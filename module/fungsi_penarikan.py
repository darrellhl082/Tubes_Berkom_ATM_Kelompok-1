# Program Fungsi Penarikan ATM
# saldo = 5000000
from PIL import Image # type: ignore

min_saldo = 50000
def penarikan_tunai(nasabah_now, jumlah_penarikan):
    while True:
        if jumlah_penarikan == None:     
            while True:
                jumlah_penarikan = int(input("Rp"))
                if jumlah_penarikan%50000 != 0:
                    print("SILAHKAN MASUKKAN ULANG JUMLAH UANG YANG INGIN ANDA TARIK")
                    pass
                elif jumlah_penarikan%50000 == 0:
                    break
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
            break
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
            saldo_text = f"SISA SALDO ANDA {nasabah_now["saldo"]}".center(40)
            print(
        f"""
        __________________________________________
        |                                        |
        |                                        |
        |            TRANSAKSI BERHASIL          |
        |      SILAHKAN MENGAMBIL UANG ANDA      |
        |            TERIMA KASIH :)             |
        |                                        |
        |{saldo_text}|
        |                                        |
        |________________________________________|
        """
            )
            limapuluh = Image.open("assets/limapuluh.jpg")
            for _ in range(0, jumlah_penarikan//50000):
                limapuluh.show()
            break

