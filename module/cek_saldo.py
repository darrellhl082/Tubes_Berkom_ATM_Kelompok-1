def cek_saldo(data_nasabah_online):
    print(
        f"""
        __________________________________________
        |                                        |
        |              JUMLAH SALDO              |
        |                                        |
        |     {data_nasabah_online["Saldo"]}     |
        |                 RUPIAH                 |
        |                                        |
        |     APAKAH INGIN LANJUT TRANSAKSI?     |
        | (1) YA                      (2) TIDAK  |
        |________________________________________|
        """)

    input_pilihan = input("Pilih menu: ")
    if input_pilihan == 2:
        quit()