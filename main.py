# Program Simulasi ATM
# Lorem Ipsum

# Kamus

# Variabel
# main_loop: bool

# Fungsi


# Algoritma
#

# Import fungsi

# from module.hello import hello


# Definisi Variabel dan Array

# Definisi Fungsi

def penarikan_tunai(jumlah):
    print(jumlah)

def main():
    main_loop = True

    while main_loop:

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

        list_nominal = [50000, 250000, 500000, 750000, 1000000, 1500000, None]
        if input_pilihan_menu < 7:
            penarikan_tunai(list_nominal[input_pilihan_menu - 1])
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
                    print("informasi_saldo()")
                    break
                elif input_pilihan_menu == 2:
                    print("transfer bank")
                    break
                elif input_pilihan_menu == 3:
                    break
                else:
                    input_pilihan_menu = int(input("Pilih menu: "))


    
        
        # Loop Termination
        
        if not main_loop: # Loop Terminator
            break



# Main Loop
main()







