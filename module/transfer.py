# Program Transfer ATM

min_saldo = 50000

def transfer(data_nasabah, nasabah_now):
    rekening_tujuan = dict()

    while True:
        print("TRANSFER")

        # Validasi rekening tujuan
        found = False
        while not found:
            print("MASUKKAN NOMOR REKENING TUJUAN")
            norek = str(input())   
            for item in data_nasabah:
                if norek == item["nomor_rekening"]:
                    rekening_tujuan = item
                    print("NOMOR REKENING:", item["nomor_rekening"])
                    print("NAMA:", item["nama"])
                    found = True
                else:
                    pass
            if not rekening_tujuan:
                print("NOMOR REKENING TIDAK DITEMUKAN")
        
        pilih = input("1. TEKAN 1 JIKA BENAR\n2. TEKAN 2 JIKA SALAH\n")
        if pilih == "1":
            while True:
                print("MASUKKAN JUMLAH NOMINAL YANG AKAN DITRANSFER")
                nominal_transfer = int(input())

                konfirmasi = input("1. TEKAN 1 JIKA BENAR\n2. TEKAN 2 JIKA SALAH\n3. TEKAN CANCEL UNTUL PEMBATALAN\n")
                if konfirmasi == "1":
                    if nominal_transfer > nasabah_now["saldo"]:
                        print("SALDO ANDA TIDAK MENCUKUPI")
                    elif nasabah_now["saldo"] < min_saldo:  # min_saldo = 50000
                        print("SALDO ANDA TIDAK MENCUKUPI")
                    elif nasabah_now["saldo"]-nominal_transfer < min_saldo: # min_saldo = 50000
                        print("SALDO ANDA TIDAK MENCUKUPI")
                    else:
                        nasabah_now["saldo"] -= nominal_transfer
                        rekening_tujuan["saldo"] += nominal_transfer
                        print("INVOICE")
                        print(f"SALDO ANDA SAAT INI {nasabah_now["saldo"]}")

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
