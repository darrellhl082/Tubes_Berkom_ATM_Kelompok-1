def cek_saldo(nasabah_now):
    saldo_text = f"{nasabah_now["saldo"]}".center(40)
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
        """)

    input_pilihan = input("Pilih menu: ")
    if input_pilihan == 2:
        quit()