# Program: Prosedur Pengecekan Saldo
# Spesifikasi: Prosedur untuk menampilkan saldo pengguna (nasabah) yang sedang menggunakan program 

# KAMUS
# main_loop_config.main_loop: bool; variabel dari file main_loop_config.py yang digunakan untuk melanjutkan/memberhentikan perulangan pada main.py.

# ALGORITMA
from module import main_loop_config # mengambil kode dalam main_loop_config.py untuk variabel main_loop digunakan dalam program

# Definisi prosedur
def cek_saldo(nasabah_now): # parameter nasabah_now bertipe dict, bertujuan untuk menampung data pengguna
    # Menampilkan saldo pengguna dan memerintah main untuk berhenti berulang jika diinginkan pengguna

    # KAMUS LOKAL
    # saldo_text: str; jumlah saldo (dicenter dalam kotak)
    # input_pilihan: str; pilihan lanjut atau tidak

    # Algoritma
    saldo_text = f"{nasabah_now["saldo"]}".center(40) # meng-center string pada output
    print(
        f"""
        __________________________________________
        |                                        |
        |              JUMLAH SALDO              |
        |                                        |
        |{saldo_text}|
        |                 RUPIAH                 |
        |                                        |
        |     APAKAH INGIN LANJUT TRANSAKSI?     |
        | (1) YA                      (2) TIDAK  |
        |________________________________________|
        """) # output

    # Memberi pengguna pilihan untuk lanjut atau tidak
    input_pilihan = int(input("Pilih menu: "))
    if input_pilihan == 2:
        main_loop_config.main_loop = False # Update variable tersebut menjadi false yang nantinya akan menandakkan keberhentian dari pengulangan pada main