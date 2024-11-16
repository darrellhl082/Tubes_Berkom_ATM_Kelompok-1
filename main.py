# Program Simulasi ATM
# Lorem Ipsum

# KAMUS
# -

# Algoritma

# Import fungsi dan prosedur dari berbagai file serta module
from module.data_nasabah import data_nasabah
from module.main_autentikasi import Main_Otentikasi # fungsi autentikasi
from module.cek_saldo import cek_saldo # fungsi cek saldo
from module.fungsi_penarikan import penarikan_tunai
from module.transfer import transfer
from module import main_loop_config
from time import sleep

# Definisi prosedur
def main():

    # Program bagian utama pada ATM yang akan menampilkan menu dan mengeksekusi fungsi/prosedur pada ATM secara berulang hingga diberhentikan

    # KAMUS LOKAL
    # saldo_text: str; jumlah saldo (dicenter dalam kotak)
    # input_pilihan_menu: str; memegang input pilihan menu
    # nasabah_now: dict; memegang data pengguna
    # list_nominal: list of integers; nominal-nominal penarikan

    main_loop_config.main_loop = True # Inisialisasi untuk memastikan prosedur akan diulang hingga diberhentikan oleh pengguna
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
        | (0) CANCEL                             |
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
        | (0) CANCEL                             |
        | (1) INFORMASI SALDO                    |
        | (2) TRANSFER ANTAR BANK                |
        | (3) PENARIKAN TUNAI                    |
        |________________________________________|
        """
            ) # Penampilan menu kedua

            # Rangkaian instruksi meminta input pengguna hingga terdapat input yang ada opsinya
            input_pilihan_menu = int(input("Pilih menu: "))
            while True:  
                if input_pilihan_menu < 0 or input_pilihan_menu > 3:
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
                
        
        # Loop Termination        
        if not main_loop_config.main_loop: # Loop Terminator
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