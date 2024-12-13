# Program Transfer ATM
# Memungkinkan nasabah untuk memindahkan uang dari satu rekening bank ke rekening bank lainnya

# KAMUS
# rekening_tujuan : array of dict
# norek : str
# pilih, nominal_transfer, konfirmasi : int

# ALGORITMA

min_saldo = 50000

def transfer(data_nasabah, nasabah_now):
    rekening_tujuan = dict()

    while True:
        # validasi rekening tujuan
        found = False
        while not found:
            print(
            """
        __________________________________________
        |                                        |
        |                TRANSFER                |
        |                                        |
        |     MASUKKAN NOMOR REKENING TUJUAN     |
        |                                        |
        |                                        |
        |                                        |
        |                                        |
        |________________________________________|
            """
            )
            norek = str(input())   
            for item in data_nasabah:
                # jika nomor rekening terdaftar, program akan menampilkan identitas nasabah untuk mengonfirmasi
                if norek == item["nomor_rekening"] and norek != nasabah_now["nomor_rekening"]:
                    rekening_tujuan = item
                    norek_tujuan_text = f"NOMOR REKENING {item["nomor_rekening"]}".center(40)
                    nama_text = f"NAMA: {item["nama"]}".center(40)
                    print(
                    f"""
        __________________________________________
        |                                        |
        |                TRANSFER                |
        |                                        |
        |{norek_tujuan_text}|
        |{nama_text}|
        |                                        |
        |                  (1) TEKAN JIKA BENAR  |
        |                  (2) TEKAN JIKA SALAH  |
        |________________________________________|
                    """
                    )
                    found = True  
                else:
                    pass
            if not rekening_tujuan:
                norek_text = f"NOMOR REKENING {norek}".center(40)
                print(
                f"""
        __________________________________________
        |                                        |
        |                TRANSFER                |
        |                                        |
        |{norek_text}|
        |                                        |            
        |                                        |
        |     NOMOR REKENING TIDAK DITEMUKAN     |
        |                                        |
        |________________________________________|
                """
                )
                
        # input nominal transfer
        pilih = int(input())
        if pilih == "1":
            while True:
                print(
                """
        __________________________________________
        |                                        |
        |                TRANSFER                |
        |                                        |
        |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
        |                                        |
        |                                        |
        |                                        |
        |                                        |
        |________________________________________|
                """
                )
                nominal_transfer = int(input())
                nominal_text = f"{nominal_transfer}".center(40)

                konfirmasi = int(input(
                f"""
        __________________________________________
        |                                        |
        |                TRANSFER                |
        |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
        |{nominal_text}|
        |                                        |
        |                            (0) CANCEL  |
        |                  (1) TEKAN JIKA BENAR  |
        |                  (2) TEKAN JIKA SALAH  |
        |________________________________________|
                """
                ))
                if konfirmasi == "1":
                    if nominal_transfer > nasabah_now["saldo"]:
                        print(
                        f"""
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
                    elif nasabah_now["saldo"] < min_saldo:  # min_saldo = 50000
                        print(
                        f"""
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
                    elif nasabah_now["saldo"]-nominal_transfer < min_saldo: # min_saldo = 50000
                        print(
                        f"""
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
                        nasabah_now["saldo"] -= nominal_transfer
                        rekening_tujuan["saldo"] += nominal_transfer
                        
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
                        # update data_nasabah menjadi nasabah_now
                        for item in data_nasabah:
                            if(item["nomor_rekening"] == nasabah_now["nomor_rekening"]):
                                item = nasabah_now
                                break

                        # update data di rekening_tujuan
                        for item in data_nasabah:
                            if(item["nomor_rekening"] == rekening_tujuan["nomor_rekening"]):
                                item = rekening_tujuan
                                break
                        break

                elif konfirmasi == "2":
                    # nge loop ulang ke input nominal transfer,tterus masukin ulang lagi
                    pass
                elif konfirmasi == "0":
                    quit()
            break
            
        elif pilih == "2":
            # nge loop ulang ke input norek, terus masukin ulang lagi
            pass