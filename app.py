from flask import Flask, render_template, request, send_file, redirect, url_for
import requests
import os
from io import BytesIO
import threading
import time
from dotenv import load_dotenv
import base64

app = Flask(__name__)

load_dotenv()  # take environment variables

# Folder untuk simpan upload dan hasil sementara
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_URL = os.getenv("API_URL")
API_BEARER = os.getenv("API_BEARER")
# Fungsi hapus file setelah delay
def delete_file_later(filepath, delay=30):
    def delete():
        time.sleep(delay)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"[INFO] File deleted: {filepath}")
    threading.Thread(target=delete).start()

@app.route('/', methods=['GET', 'POST'])
def index():
    original_image_url = None
    enhanced_image_url = None

    if request.method == 'POST':
        image_file = request.files.get('image')
        if image_file:
            filename = image_file.filename
            original_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(original_path)

            # Jadwalkan hapus file asli setelah 30 detik
            delete_file_later(original_path)

            # Kirim ke Vyro API
            with open(original_path, 'rb') as f:
                files = {'image': f}
                headers = {'Authorization': API_BEARER}  # <- Pastikan ini adalah string, bukan set atau dict
                data = {'model_version': '1'}
                response = requests.post(API_URL, headers=headers, files=files, data=data)

          
            if response.status_code == 200:
                enhanced_bytes = response.content
                enhanced_base64 = base64.b64encode(enhanced_bytes).decode('utf-8')

                original_base64 = base64.b64encode(open(original_path, 'rb').read()).decode('utf-8')

                original_image_url = f"data:image/jpeg;base64,{original_base64}"
                enhanced_image_url = f"data:image/jpeg;base64,{enhanced_base64}"


    return render_template('index.html',
                           original_image=original_image_url,
                           enhanced_image=enhanced_image_url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

if __name__ == '__main__':
    app.run(debug=True)
