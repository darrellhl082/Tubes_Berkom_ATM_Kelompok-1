# Program ATM

## Deskripsi
Program Simulasi ATM ini ditujukan untuk memenuhi tugas besar mata kuliah Berpikir Komputasi. Fungsionalitas program ini mengambil dasar dari mesin ATM sebenarnya. Terdapat beberapa fitur esensial ATM seperti penarikan tunai, setor tunai, dan transfer antarbank. Program ini disusun oleh kelompok 1 - K25 dengan anggota:
- Jessen Gosal   		 (16524002)
- Darfis Ahmad D.	   (16524007)
- Rahmia Khairanti	 (16524010)
- Muhammad Zaki A.S. (16524036)
- Darrell Hammam L.  (16524042)
- Audrey Nabiilah P. (16524052)

## Fitur
- **Tarik Tunai:** pengguna dapat melakukan penarikan uang tunai dari rekening
- **Setor Tunai:** pengguna dapat melakukan penyetoran uang tunai ke rekening
- **Transfer:** pengguna dapat melakukan transfer saldo rekeningnya ke rekening lain
- **Cek Saldo:** pengguna dapat mengecek saldo rekeningnya saat ini
- **Autentikasi:** pengguna harus memasukkan nomor rekening dan kata sandinya untuk mengakses rekening
- **Database Dinamis:** data rekening pengguna tersimpan di sebuah basis data dinamis agar data tetap terjaga walau siklus hidup program selesai

## Instalasi
   Disarankan melakukan instalasi melalui halaman repositori GitHub. Sebelum memulai program, pastikan denpendensi program sudah terpasang. Jika belum, dapat mengikuti petunjuk di bawah ini.
1. **Clone Repository**
```bash
   git clone https://github.com/darrellhl082/Tubes_Berkom_ATM_Kelompok-1.git
```
2. **Masuk ke Direktori Projek**
```bash
   cd Tubes_Berkom_ATM_Kelompok-1
```
3. **Install Dependensi**
```bash
   pip install -r requirements.txt
```
4. **Jalankan Aplikasi**
```bash
   python main.py
```

## Penggunaan
1. **Autentikasi:** masukkan nomor rekening dan kata sandi yang tertera di dokumen data_nasabah.json.
   Contoh: 16524001 (NoRek) | 230224 (Kata Sandi)
3. **Tarik Tunai:** pilih menu nominal atau nomor 8 dan masukkan nominal dalam kelipatan Rp50.000
4. **Setor Tunai:** masukkan jumlah lembar uang dengan kelipatan Rp50.000 setiap lembar untuk disetor
5. **Cek Saldo:** pergi ke menu transaksi lainnya dan pilih menu cek saldo
6. **Database:** pastikan mematikan program secara normal dengan pilih nomor 0 atau QUIT di menu agar database diperbarui

## Kontak Kelompok
- **Nama:** Darrell Hammam Luthiadi
- **NIM:** 16524042
- **Email:** darrellhluthfiadi@gmail.com






