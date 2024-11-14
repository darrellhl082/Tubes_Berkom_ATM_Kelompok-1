# Program Simulasi ATM
# Lorem Ipsum

# Kamus

# Variabel
# main_loop: bool

# Fungsi


# Algoritma
#

# Import fungsi
from module.data_nasabah import data_nasabah
from module.main_autentikasi import Main_Otentikasi # fungsi autentikasi
from module.cek_saldo import cek_saldo # fungsi cek saldo
from module.fungsi_penarikan import penarikan_tunai
from module.transfer import transfer
from module import main_loop_config
# Definisi Variabel dan Array

# Definisi Fungsi

def main():
    main_loop_config.main_loop = True
    nasabah_now = Main_Otentikasi(data_nasabah)
    while main_loop_config.main_loop:

        # Kondisi Menu
        print(
        """
        __________________________________________
        |                                        |
        |            PENARIKAN TUNAI             |
        | SILAHKAN MASUKKAN ANGKA SESUAI PILIHAN |
        |                                        |
        | (1) 50.000      (5) 1.000.000          |
        | (2) 250.000     (6) 1.500.000          |
        | (3) 500.000     (7) Jumlah Lainnya     |
        | (4) 750.000     (8) Transaksi Lainnya  |
        |________________________________________|
        """
        )
        input_pilihan_menu = int(input("Pilih menu: "))
        while True:  
            if input_pilihan_menu < 0 or input_pilihan_menu > 8:
                input_pilihan_menu = int(input("Opsi tidak ditemukan. Pilih menu: "))
            else:
                break

        list_nominal = [50000, 250000, 500000, 750000, 1000000, 1500000, None]
        if input_pilihan_menu < 8:
            penarikan_tunai(nasabah_now, list_nominal[input_pilihan_menu - 1])
        elif input_pilihan_menu == 8:
            print(
        """
        __________________________________________
        |                                        |
        |             TRANSAKSI LAIN             |
        | SILAHKAN MASUKKAN ANGKA SESUAI PILIHAN |
        |                                        |
        | (1) INFORMASI SALDO                    |
        | (2) TRANSFER ANTAR BANK                |
        | (3) PENARIKAN TUNAI                    |
        |                                        |
        |________________________________________|
        """
            )
            input_pilihan_menu = int(input("Pilih menu: "))
            while True:           
                if input_pilihan_menu == 1:
                    cek_saldo(nasabah_now)
                    break
                elif input_pilihan_menu == 2:
                    transfer(data_nasabah, nasabah_now)
                    break
                elif input_pilihan_menu == 3:
                    break
                else:
                    input_pilihan_menu = int(input("Opsi tidak ditemukan. Pilih menu: "))


    
        
        # Loop Termination
        
        if not main_loop_config.main_loop: # Loop Terminator
            break



# Main Loop
main()







