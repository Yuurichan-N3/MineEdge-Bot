# 🌟 MineEdge Bot - Ad Reward Claim

Script Python untuk mengotomatiskan klaim hadiah iklan di MineEdge. Dirancang untuk mempermudah pengguna dalam mengelola beberapa akun dengan antarmuka yang kaya dan informatif menggunakan `rich`.

---

## 🚀 Fitur Utama
- Membaca `initData` dari file `data.txt` untuk multiple akun
- Mengotomatiskan klaim hadiah iklan melalui API
- Logging real-time dengan timestamp dan status
- Tabel ringkasan hasil klaim
- Penanganan error yang ramah pengguna
- Delay antar request untuk mencegah spam

---

## 📋 Prasyarat
Sebelum memulai, pastikan Anda memiliki:
- Python (versi 3.7 atau lebih tinggi) terinstal
- Library Python berikut:
  - `requests`
  - `rich`
- File `data.txt` berisi `initData` untuk setiap akun (satu per baris)

---

## 🛠️ Cara Instalasi
1. **Clone Repository**
   ```bash
   git clone https://github.com/Yuurichan-N3/MineEdge-Bot.git
   cd MineEdge-bot
   ```

2. **Instal Dependensi**
   Jalankan perintah berikut untuk menginstal library yang dibutuhkan:
   ```bash
   pip install requests rich
   ```

3. **Siapkan File `data.txt`**
   - Buat file `data.txt` di direktori yang sama dengan script
   - Masukkan `initData` untuk setiap akun, satu per baris, contoh:
     ```
     initData1
     initData2
     initData3
     ```
   - Pastikan data valid dan sesuai dengan format yang diharapkan API

---

## ▶️ Cara Penggunaan
1. **Jalankan Script**
   Dari terminal, ketik:
   ```bash
   python bot.py
   ```

2. **Ikuti Prompt**
   - Setelah banner ditampilkan, masukkan jumlah request yang diinginkan
   - Script akan memproses setiap request dan menampilkan log status

3. **Pantau Output**
   - Log akan menampilkan status setiap request (SUCCESS/FAILED) dengan timestamp
   - Tabel ringkasan akan muncul di akhir, menunjukkan hasil untuk setiap request
   - Contoh output:
     ```
     [2025-04-07 10:00:00] INFO: Request #1 (Akun #1) | Status: SUCCESS | Ad reward claimed successfully!
     ```

4. **Hentikan Jika Diperlukan**
   Tekan `Ctrl+C` untuk menghentikan eksekusi kapan saja

---

## 📂 Struktur File
- `bot.py`: Script utama
- `data.txt`: File input berisi initData (harus dibuat manual)
- `README.md`: Dokumentasi ini

---

## ⚠️ Catatan Penting
- Pastikan koneksi internet stabil
- File `data.txt` harus ada dan berisi minimal satu `initData`
- Script akan berhenti jika input jumlah request tidak valid
- Delay 3 detik antar request untuk menghindari pemblokiran

---

## 📜 Lisensi
Script ini didistribusikan untuk keperluan pembelajaran dan pengujian. Penggunaan di luar tanggung jawab pengembang.

Untuk update terbaru, bergabunglah di grup **Telegram**: [Klik di sini](https://t.me/sentineldiscus).

---

## 💡 Disclaimer
Penggunaan bot ini sepenuhnya tanggung jawab pengguna. Kami tidak bertanggung jawab atas penyalahgunaan skrip ini.
