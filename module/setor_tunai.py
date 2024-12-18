# Program Setor Tunai

def setor_tunai(data_nasabah, nasabah_now):
    status = False
    while not status:
        print(
        """
        __________________________________________
        |                                        |
        |                                        |
        |                                        |
        |       SILAHKAN MASUKKAN UANG ANDA      |
        |          MAKSIMAL 100 LEMBAR           |
        |                                        |
        |                                        |
        |                                        |
        |________________________________________|
        """
            )
        jumlah_setor = int(input("Masukkan jumlah lembar uang: "))
        if 0 < jumlah_setor <= 100:
            total = 50000*jumlah_setor
            total_text = f"50000 x {jumlah_setor} = {total}".center(40)
            print(
            f"""
            __________________________________________
            |                                        |
            |                                        |
            |                                        |
            |                                        |
            |{total_text}|
            |                                        |
            |                            (0) CANCEL  |
            |                            (1) SETOR   |
            |________________________________________|
            """
                )
            konfirmasi = int(input(""))
            if konfirmasi == 1:
                nasabah_now["saldo"] = nasabah_now["saldo"] + total
              
                sisa_text = f"SISA SALDO ANDA {nasabah_now["saldo"]}".center(40)

                print(
                f"""
            __________________________________________
            |                                        |
            |                                        |
            |            TRANSAKSI BERHASIL          |
            |              TERIMA KASIH :)           |
            |                                        |
            |                                        |
            |{sisa_text}|
            |                                        |
            |________________________________________|
                """
                )
                for item in data_nasabah:
                    if(item["nomor_rekening"] == nasabah_now["nomor_rekening"]):
                        item = nasabah_now
                        break
                status = True
            elif konfirmasi == 0:
                status = True
        else:
            print(
        """
        __________________________________________
        |                                        |
        |                                        |
        |                                        |
        |              TIDAK VALID               |
        |                                        |
        |                                        |
        |                                        |
        |                                        |
        |________________________________________|
        """
            )

