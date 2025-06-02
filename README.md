# Image Enhancer API dengan Flask dan Vyro AI

Proyek ini menyediakan API sederhana untuk meningkatkan kualitas gambar menggunakan Python, framework Flask untuk web, dan berinteraksi dengan API Vyro AI untuk pemrosesan gambar.

## Deskripsi

API Image Enhancer memungkinkan pengguna untuk mengunggah gambar dan menerima kembali gambar yang telah ditingkatkan kualitasnya. Proses peningkatan kualitas gambar didelegasikan ke layanan API **Vyro AI**. Aplikasi Flask ini bertindak sebagai perantara untuk mengirimkan gambar ke Vyro AI dan mengembalikan hasilnya kepada pengguna.

## Fitur

* Menerima unggahan gambar melalui HTTP POST request.
* Mengirimkan gambar yang diunggah ke API **Vyro AI** untuk peningkatan kualitas.
* Menerima gambar yang telah ditingkatkan dari **Vyro AI**.
* Mengembalikan gambar yang telah ditingkatkan sebagai response HTTP kepada pengguna.
* Menggunakan Flask sebagai framework web mikro.
* Menggunakan library Requests untuk berinteraksi dengan API **Vyro AI**.

## Cara Penggunaan

### Prasyarat

* **Python 3.x** terinstal di sistem Anda.
* **pip** (Python package installer) terinstal.
* **Akun Vyro AI** dan **API Key** yang valid. Anda perlu mendaftar di platform Vyro AI untuk mendapatkan API Key.

### Instalasi

1.  Clone repositori ini (jika ada) atau buat direktori proyek baru.
2.  Navigasi ke direktori proyek.
3.  Instal dependensi yang diperlukan menggunakan pip:
    ```bash
    pip install Flask requests
    ```

### Konfigurasi

1.  Buat(misalnya, `.env`) gunakan environment variables untuk menyimpan API Key Vyro AI Anda.

    **Contoh `.env`:**
    ```python
    VYRO_API_KEY = "YOUR_VYRO_AI_API_KEY"
    VYRO_API_URL = "URL_API_VYRO_AI_UNTUK_PENINGKATAN_GAMBAR" # Sesuaikan dengan endpoint Vyro AI
    ```

2.  Pastikan aplikasi Flask Anda (`app.py`) dapat mengakses konfigurasi ini.

### Menjalankan Aplikasi

1.  Pastikan file utama aplikasi Flask Anda (misalnya, `app.py`) berada di direktori proyek dan telah dikonfigurasi untuk menggunakan API Key Vyro AI.
2.  Jalankan aplikasi Flask dari terminal:
    ```bash
    python app.py
    ```
    atau jika Anda menggunakan environment variables untuk konfigurasi Flask:
    ```bash
    flask run
    ```
    (Pastikan `FLASK_APP` environment variable telah diatur ke nama file aplikasi Anda).

3.  Server Flask akan berjalan (biasanya di `http://127.0.0.1:5000/`).

### Menggunakan API

Anda dapat mengirimkan request POST ke endpoint yang ditentukan untuk mengunggah gambar dan menerima gambar yang ditingkatkan dari Vyro AI. Berikut adalah contoh menggunakan `curl`:

```bash
curl -X POST -H "Authorization: Bearer YOUR_VYRO_AI_API_KEY" -F "image=@/path/ke/gambar/anda.jpg" [http://127.0.0.1:5000/enhancer](http://127.0.0.1:5000/enhancer)
