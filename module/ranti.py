# Program Fungsi Penarikan ATM
# Python

def penarikan_tunai():
    print("PENARIKAN TUNAI")
    """
    50000
    250000
    500000
    750000
    1000000
    1250000
    1500000
    """
    nominal = ["50000", "250000", "500000", "750000", "1000000", "1250000", "1500000"]
    for data in nominal:
        print(data)
penarikan_tunai()

def penarikan_jumlah_lain():
    print("PENARIKAN JUMLAH LAIN")
    print("MASUKKAN JUMLAH UANG YANG AKAN DITARIK")

saldo = 5000000
min_saldo = 50000

while True:
    penarikan_jumlah_lain()
    jumlah_tarik = int(input("Rp"))
    pilih = input("1. TEKAN 1 JIKA BENAR \n2. TEKAN 2 JIKA KOREKSI\n")
    if pilih == "1":
        if jumlah_tarik > saldo:
            print("SALDO ANDA TIDAK MENCUKUPI")
        elif saldo < min_saldo:
            print("SALDO ANDA TIDAK MENCUKUPI")
        elif saldo-jumlah_tarik < min_saldo:
            print("TRANSAKSI GAGAL")
            print("SALDO ANDA TIDAK MENCUKUPI")
        else:
            print("TRANSAKSI BERHASIL")
            print("SILAHKAN MENGAMBIL UANG ANDA")
            saldo = saldo - jumlah_tarik
            print("SISA SALDO ANDA", saldo)
            break
    elif pilih == "2":
        # koreksi jumlah penarikan yang ingin diambil, terus masukin ulang lagi
        pass