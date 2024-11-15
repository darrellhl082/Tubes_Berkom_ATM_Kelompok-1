# Program Transfer ATM

min_saldo = 50000

def transfer(data_nasabah, nasabah_now):
    rekening_tujuan = dict()

    while True:
        # Validasi rekening tujuan
        found = False
        while not found:
            print(
            """
            __________________________________________
            |              A T M TRANSFER            |
            |                                        |
            |     MASUKKAN NOMOR REKENING TUJUAN     |
            |                                        |
            |                                        |
            |                                        |
            |                                        |
            |                                        |
            |________________________________________|
            """
            )
            norek = str(input())   
            for item in data_nasabah:
                if norek == item["nomor_rekening"]:
                    rekening_tujuan = item
                    print(
                    f"""
                    __________________________________________
                    |              A T M TRANSFER            |
                    |                                        |
                    |                                        |
                    |        NOMOR REKENING: {item["nomor_rekening"]}        |
                    |        NAMA: {item["nama"]}                     |
                    |                                        |
                    |                 1. TEKAN 1 JIKA BENAR  |
                    |                 2. TEKAN 2 JIKA SALAH  |
                    |________________________________________|
                    """
                    )
                    found = True
                else:
                    pass
            if not rekening_tujuan:
                print(
                f"""
                __________________________________________
                |              A T M TRANSFER            |
                |                                        |
                |                                        |
                |         NOMOR REKENING:{norek}        |
                |                                        |            
                |                                        |
                |     NOMOR REKENING TIDAK DITEMUKAN     |
                |                                        |
                |________________________________________|
                """
                )
                
        
        pilih = input()
        if pilih == "1":
            while True:
                print(
                """
                __________________________________________
                |              A T M TRANSFER            |
                |                                        |
                |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
                |                                        |
                |                                        |
                |                                        |
                |                                        |
                |                                        |
                |________________________________________|
                """
                )
                nominal_transfer = int(input())

                konfirmasi = input(
                f"""
                __________________________________________
                |              A T M TRANSFER            |
                |                                        |
                |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
                |           {nominal_transfer}                 |
                |                                        |
                |                 1. TEKAN 1 JIKA BENAR  |
                |                 2. TEKAN 2 JIKA SALAH  |
                |      3. TEKAN CANCEL UNTUL PEMBATALAN  |
                |________________________________________|
                """
                )
                if konfirmasi == "1":
                    if nominal_transfer > nasabah_now["saldo"]:
                        print(
                        f"""
                        __________________________________________
                        |              A T M TRANSFER            |
                        |                                        |
                        |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
                        |                {nominal_transfer}                 |
                        |                                        |
                        |                                        |
                        |       SALDO ANDA TIDAK MENCUKUPI       |
                        |                                        |
                        |________________________________________|
                        """
                        )
                    elif nasabah_now["saldo"] < min_saldo:  # min_saldo = 50000
                        print(
                        f"""
                        __________________________________________
                        |              A T M TRANSFER            |
                        |                                        |
                        |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
                        |                {nominal_transfer}                 |
                        |                                        |
                        |                                        |
                        |       SALDO ANDA TIDAK MENCUKUPI       |
                        |                                        |
                        |________________________________________|
                        """
                        )
                    elif nasabah_now["saldo"]-nominal_transfer < min_saldo: # min_saldo = 50000
                        print(
                        f"""
                        __________________________________________
                        |              A T M TRANSFER            |
                        |                                        |
                        |    MASUKKAN JUMLAH NOMINAL TRANSFER    |
                        |                {nominal_transfer}                 |
                        |                                        |
                        |                                        |
                        |       SALDO ANDA TIDAK MENCUKUPI       |
                        |                                        |
                        |________________________________________|
                        """
                        )
                    else:
                        nasabah_now["saldo"] -= nominal_transfer
                        rekening_tujuan["saldo"] += nominal_transfer
                        print(
                        f"""
                        __________________________________________
                        |              A T M TRANSFER            |
                        |                                        |
                        |            TRANSFER BERHASIL           |
                        |                     {nominal_transfer}                 |
                        |                                        |
                        |           SALDO ANDA SAAT INI          |
                        |                     {nasabah_now["saldo"]}             |
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
                elif konfirmasi == "3":
                    quit()
            break
            
        elif pilih == "2":
            # nge loop ulang ke input norek, terus masukin ulang lagi
            pass
