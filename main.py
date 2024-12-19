# Program Simulasi ATM
# Lorem Ipsum

# KAMUS
# -

# Algoritma

# Import fungsi dan prosedur dari berbagai file serta module
from module.main_autentikasi import Main_Otentikasi # fungsi autentikasi
from module.cek_saldo import cek_saldo # fungsi cek saldo
from module.fungsi_penarikan import penarikan_tunai # fungsi penarikan tunai
from module.transfer import transfer # fungsi transfer
from module import main_loop_config # variabel main_loop untuk penanda online/offline (quit)
from module.setor_tunai import setor_tunai # fungsi setor tunai
from time import sleep # fungsi delay untuk meningkatkan keaslian program (terasa seperti ATM beneran)
import json # fungsi json untuk impor/ekspor json

# Definisi prosedur
def main():

    # Program bagian utama pada ATM yang akan menampilkan menu dan mengeksekusi fungsi/prosedur pada ATM secara berulang hingga diberhentikan

    # KAMUS LOKAL
    # main_loop_config.main_loop: bool; menandakan jika prosedur akan berulang atau tidak
    # input_pilihan_menu: str; memegang input pilihan menu
    # json_data_r: json type; memegang isi dari database json untuk dibaca oleh program
    # json_data_w: json type; memegang isi dari database json untuk diedit oleh program
    # data_nasabah: list (list of dictionaries, dictionary of str, int); memegang seluruh data pengguna yang diimport dari database json
    # nasabah_now: dict; memegang data pengguna yang menggunakan mesin ATM
    # list_nominal: list of integers; nominal-nominal penarikan

    main_loop_config.main_loop = True # Inisialisasi untuk memastikan prosedur akan diulang hingga diberhentikan oleh pengguna

    # Inisialisasi data_nasabah list of dictionaries dari json
    with open("module/data_nasabah.json", "r") as json_data_r:
        data_nasabah = json.load(json_data_r)

    nasabah_now = Main_Otentikasi(data_nasabah) # Memegang data pengguna dalam variabel nasabah_now
    sleep(1.0) # Menunda eksekusi kode line selanjutnya selama x (1.5) detik

    while main_loop_config.main_loop: # Pengulangan jika main_loop pada file main_loop_config.py bernilai True
        sleep(0.5)
        # Kondisi Menu
        print(
        """
        __________________________________________
        |                                        |
        |            PENARIKAN TUNAI             |
        | SILAHKAN MASUKKAN ANGKA SESUAI PILIHAN |
        | (0) QUIR                               |
        | (1) 50.000      (5) 1.000.000          |
        | (2) 250.000     (6) 1.500.000          |
        | (3) 500.000     (7) JUMLAH LAINNYA     |
        | (4) 750.000     (8) TRANSAKSI LAINNYA  |
        |________________________________________|
        """
        ) # Penampilan awal menu

        # Rangkaian instruksi meminta input pengguna hingga terdapat input yang ada opsinya
        input_pilihan_menu = int(input("Pilih menu: "))
        while True:  
            if input_pilihan_menu < 0 or input_pilihan_menu > 8:
                input_pilihan_menu = int(input("Opsi tidak ditemukan. Pilih menu: "))
            else:
                break

        sleep(0.5)
        list_nominal = [50000, 250000, 500000, 750000, 1000000, 1500000, None] # List opsi nominal penarikan

        # Pemberhentian program jika input = 0
        if input_pilihan_menu == 0:
            main_loop_config.main_loop = False

        # Penarikan, memanggil fungsi penarikan_tunai dan menggunakan nominal pada list_nominal yang sesuai
        elif input_pilihan_menu < 8:
            penarikan_tunai(nasabah_now, list_nominal[input_pilihan_menu - 1])
        
        # Bagian transaksi lainnya
        elif input_pilihan_menu == 8:
            print(
        """
        __________________________________________
        |                                        |
        |             TRANSAKSI LAIN             |
        | SILAHKAN MASUKKAN ANGKA SESUAI PILIHAN |
        |                                        |
        | (0) QUIT                               |
        | (1) INFORMASI SALDO                    |
        | (2) TRANSFER ANTAR BANK                |
        | (3) SETOR TUNAI                        |
        | (4) PENARIKAN TUNAI                    |
        |________________________________________|
        """
            ) # Penampilan menu kedua

            # Rangkaian instruksi meminta input pengguna hingga terdapat input yang ada opsinya
            input_pilihan_menu = int(input("Pilih menu: "))
            while True:  
                if input_pilihan_menu < 0 or input_pilihan_menu > 4:
                    input_pilihan_menu = int(input("Opsi tidak ditemukan. Pilih menu: "))
                else:
                    break
            sleep(0.5)
            
            if input_pilihan_menu == 0: # Jika di cancel, memberhentikan perulangan 
                main_loop_config.main_loop = False
            elif input_pilihan_menu == 1: 
                cek_saldo(nasabah_now) # Cek saldo, memanggil fungsi cek_saldo dan menggunakan data pengguna 
            elif input_pilihan_menu == 2:
                transfer(data_nasabah, nasabah_now) # Transfer, memanggil fungsi transfer dan menggunakan data pengguna serta database pengguna ATM
            elif input_pilihan_menu == 3:
                setor_tunai(data_nasabah, nasabah_now)
                
        
        # Loop Termination        
        if not main_loop_config.main_loop: # Loop Terminator
            # memperbarui data untuk json database, mengubah ke json
            data_nasabah = json.dumps(data_nasabah, indent=2)

            # menulis ke json database
            with open("module/data_nasabah.json", "w") as json_data_w:
                json_data_w.write(data_nasabah)

            print(
        """
        __________________________________________
        |                                        |
        |                                        |
        |                                        |
        |              TERIMA KASIH              |
        |                                        |
        |            SAMPAI JUMPA LAGI           |
        |                                        |
        |                                        |
        |________________________________________|
        """
            ) # Penampilan sebelum keluar program
            sleep(1.5)
            break


# Eksekusi Main Loop
main()