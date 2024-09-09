# SubHunt-Scanner: Reliable and Maintainable Subdomain Finder for Security Researchers

**SubHunt** adalah sebuah alat penemuan subdomain yang dirancang ulang dengan pendekatan profesional untuk tujuan edukasi di bidang keamanan siber. Proyek ini mengimplementasikan kode yang bersih, terstruktur dengan prinsip _Object-Oriented Programming (OOP)_, dan menggunakan praktik terbaik dalam pengembangan perangkat lunak Python.

Tujuan utama SubHunt adalah untuk mendemonstrasikan cara membangun alat keamanan yang andal dan dapat dipelihara, bukan hanya sekadar skrip fungsional. Alat ini memanfaatkan data transparansi sertifikat dari `crt.sh` untuk mengidentifikasi subdomain yang terdaftar.

## 📜 Disclaimer & Ethical Use Notice

> **PENTING:** Alat ini dibuat **hanya** untuk tujuan pendidikan **dan penelitian keamanan**. Pengguna bertanggung jawab penuh atas tindakan mereka saat menggunakan SubHunt.
> 
> * **Jangan** gunakan alat ini pada domain atau sistem mana pun tanpa izin eksplisit dari pemiliknya.
> * Melakukan pemindaian tanpa izin adalah **ilegal** dan **tidak etis**.
> * Pengembang tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh alat ini. Gunakan dengan risiko Anda sendiri.

## ✨ Fitur Utama

* **Antarmuka Command-Line (CLI):** Interaksi yang efisien dan dapat diotomatisasi menggunakan `argparse`.
* **Desain Berbasis Objek (OOP):** Kode yang modular, mudah diperluas, dan mudah diuji.
* **Logging Profesional:** Output yang jelas ke konsol dan pencatatan detail ke file log (`subhunt.log`) untuk _auditing_ dan _debugging_.
* **Dua Mode Pemindaian:**
  * **Complete Scan:** Pencarian mendalam yang mencakup semua data sertifikat yang tersedia.
  * **Quick Scan:** Mode default untuk pencarian cepat (tidak termasuk sertifikat kedaluwarsa).
* **Manajemen Dependensi:** Menggunakan `requirements.txt` untuk instalasi yang mudah dan konsisten.

## 🛠️ Prasyarat & Instalasi

Sebelum memulai, pastikan Anda telah menginstal **Python 3.13** atau versi yang lebih baru.

### Langkah-langkah Instalasi:

1. **Clone Repositori**
   
   ```bash
   git clone https://github.com/RozhakDev/SubHunt-Scanner.git
   cd SubHunt-Scanner
   ```
2. **Instal Dependensi**
    SubHunt hanya memerlukan `requests`. Instal dengan perintah berikut:
   
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Cara Penggunaan

SubHunt dijalankan melalui terminal dengan menggunakan `main.py`. Berikut adalah beberapa contoh penggunaan:

**1. Menjalankan Pemindaian Cepat (Quick Scan)**

Ini adalah perintah paling dasar untuk mencari subdomain dari sebuah domain.

```bash
python main.py --domain example.com
```

**2. Menjalankan Pemindaian Lengkap (Complete Scan) dan Menyimpan Hasil**

Gunakan flag `--complete` untuk pencarian yang lebih dalam dan `--output` untuk menyimpan hasilnya ke file.

```bash
python main.py --domain example.com --output results/example.txt --complete
```

**3. Menjalankan dengan Output Verbose**

Gunakan flag `--verbose` untuk melihat log level DEBUG di konsol, yang berguna untuk melacak proses secara detail.

```bash
python main.py -d example.com -o results/example.txt --verbose
```

**Argumen yang Tersedia**

| Argumen  | Pendek | Panjang      | Deskripsi                                                               | Wajib  |
| -------- | ------ | ------------ | ----------------------------------------------------------------------- | ------ |
| Domain   | `-d`   | `--domain`   | Domain target yang akan dipindai (contoh: `example.com`).               | **Ya** |
| Output   | `-o`   | `--output`   | Path file untuk menyimpan hasil subdomain yang ditemukan.               | Tidak  |
| Complete |        | `--complete` | Mengaktifkan mode pemindaian lengkap (termasuk sertifikat kedaluwarsa). | Tidak  |
| Verbose  |        | `--verbose`  | Menampilkan log level DEBUG di konsol untuk output yang lebih detail.   | Tidak  |

## 🏗️ Struktur Proyek

Proyek ini disusun dengan struktur yang bersih dan modular untuk memisahkan setiap concern.

```text
SubHunt-Scanner/
├── main.py                # Titik masuk utama aplikasi (entry point)
├── requirements.txt       # Daftar dependensi proyek
├── subhunt/               # Paket utama aplikasi
│   ├── __init__.py
│   ├── config.py          # Menyimpan konfigurasi (seperti headers)
│   ├── finder.py          # Logika inti untuk menemukan subdomain (kelas SubdomainFinder)
│   └── logger.py          # Konfigurasi untuk logging
└── README.md              # Dokumentasi yang sedang Anda baca
```

## 🤝 Kontribusi

Kontribusi untuk meningkatkan SubHunt sangat kami hargai. Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:

1. **Fork** repositori ini.
2. Buat branch fitur baru (`git checkout -b fitur/nama-fitur-keren`).
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur keren'`).
4. Push ke branch Anda (`git push origin fitur/nama-fitur-keren`).
5. Buat **Pull Request** baru.

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.