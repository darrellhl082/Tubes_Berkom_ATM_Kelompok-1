# Program Fungsi Penarikan ATM

# saldo = 5000000
min_saldo = 50000
def penarikan_tunai(nasabah_now, jumlah_penarikan):
    while True:
        if jumlah_penarikan == None:     
            jumlah_penarikan = int(input("Rp"))
            pilih = input("1. TEKAN 1 JIKA BENAR \n2. TEKAN 2 JIKA KOREKSI\n")
            if pilih == 2:
                pass
            if jumlah_penarikan > nasabah_now["saldo"]:
                print(
                """
                __________________________________________
                |                                        |
                |                                        |
                |                                        |
                |                                        |
                |       SALDO ANDA TIDAK MENCUKUPI       |
                |                                        |
                |                                        |
                |                                        |
                |________________________________________|
                """
                )
            elif nasabah_now["saldo"] < min_saldo:
                print(
                """
                __________________________________________
                |                                        |
                |                                        |
                |                                        |
                |                                        |
                |       SALDO ANDA TIDAK MENCUKUPI       |
                |                                        |
                |                                        |
                |                                        |
                |________________________________________|
                """
                )
            elif nasabah_now["saldo"] - jumlah_penarikan < min_saldo:
                print(
                """
                __________________________________________
                |                                        |
                |                                        |
                |                                        |
                |            TRANSAKSI GAGAL             |
                |       SALDO ANDA TIDAK MENCUKUPI       |
                |                                        |
                |                                        |
                |                                        |
                |________________________________________|
                """
                )
            else:
                nasabah_now["saldo"] -= jumlah_penarikan
                print(
                f"""
                __________________________________________
                |                                        |
                |                                        |
                |            TRANSAKSI BERHASIL          |
                |      SILAHKAN MENGAMBIL UANG ANDA      |
                |            TERIMA KASIH :)             |
                |                                        |
                | SISA SALDO ANDA {nasabah_now["saldo"]} |
                |                                        |
                |________________________________________|
                """
                )
                break