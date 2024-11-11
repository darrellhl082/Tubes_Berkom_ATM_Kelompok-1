# Program Transfer ATM

# ini permisalan aja beberapa kode bank
def kode_bank():
    print("DAFTAR KODE BANK")
    bank = ["165:STEIR", "196:STEIK", "160:FMIPA", "163:FITB", "167:FTI", "166:FTSL", "169:FTMD"]
    for data in bank:
        print(data)

# permisalan aja karena belum disambungin sama yang lain
saldo = 1000000
min_saldo = 5000

while True:
    print("TRANSAKSI LAIN")
    transaksi = input("YA/TIDAK: ")
    if transaksi == "YA":
        while True:
            print("TRANSFER")
            print("MASUKKAN KODE BANK DAN NOMOR REKENING TUJUAN")
            norek = int(input())
            pilih = input("1. TEKAN 1 JIKA BENAR\n2. TEKAN 2 JIKA SALAH\n3. TEKAN 3 UNTUK KODE BANK\n")
            if pilih == "1":
                while True:
                    print("MASUKKAN JUMLAH NOMINAL YANG AKAN DITRANSFER")
                    nominalTF = int(input())
                    konfirmasi = input("1. TEKAN 1 JIKA BENAR\n2. TEKAN 2 JIKA SALAH\n3. TEKAN CANCEL UNTUL PEMBATALAN\n")
                    if konfirmasi == "1":
                        if nominalTF > saldo:
                            print("SALDO ANDA TIDAK MENCUKUPI")
                        elif saldo < min_saldo:
                            print("SALDO ANDA TIDAK MENCUKUPI")
                        elif saldo-nominalTF < min_saldo:
                            print("SALDO ANDA TIDAK MENCUKUPI")
                        else:
                            print("INVOICE")
                            break
                    elif konfirmasi == "2":
                        # nge loop ulang ke input nominal transfer,tterus masukin ulang lagi
                        pass
                    elif konfirmasi == "3":
                        quit()
            elif pilih == "2":
                # nge loop ulang ke input norek, terus masukin ulang lagi
                pass
            elif pilih == "3":
                kode_bank()
    elif transaksi == "TIDAK":
        # ceritanya balik ke menu utama
        pass
