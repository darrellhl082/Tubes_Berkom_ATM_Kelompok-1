# Program Transfer ATM

def transaksi_lain():
    print("TRANSAKSI LAIN")

def transfer():
    print("TRANSFER")

def nomor_rekening():
    print("MASUKKAN KODE BANK DAN NOMOR REKENING TUJUAN")
    norek = int(input())

# ini permisalan aja beberapa kode bank
def kode_bank():
    print("DAFTAR KODE BANK")
    bank = ["002:BRI", "009:BNI", "014:BCA", "008:MANDIRI", "100:BTN", "451:BSI", "022:CIMB NIAGA"]
    for data in bank:
        print(data)

# permisalan aja karena belum disambungin sama yang lain
saldo = 1000000
min_saldo = 50000

while True:
    transaksi_lain()
    transaksi = input("YA/TIDAK: ")
    if transaksi == "YA":
        while True:
            transfer()
            nomor_rekening()
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
