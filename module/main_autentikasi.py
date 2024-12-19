# Program: Otentikasi identitas
# Spesifikasi: Mencari nomor_rekening dan password yang sesuai


# KAMUS
# nomor_rekening: int; nomor_rekening pengguna
# password: str; password pengguna
# i, : int
# found : bool; menentukan nomor_rekening + password sdh ditemukan/belum

# ALGORITMA
# Asumsi: input array sudah dibuat; N terdefinisi


def Otentikasi(nomor_rekening, password, data_nasabah):
    found = False  # found = False; X belum ditemukan
    i = 0
    while i < len(data_nasabah) and not found: #Akan berulang hingga semua dictionary nasabah diperiksa
        if data_nasabah[i]["nomor_rekening"] == nomor_rekening and data_nasabah[i]["password"] == password:
            found = True  # found = True; nomor_rekening dan password benar
        else:
            i += 1  # hanya increment jika nomor_rekening atau password salah
    return found

def Salah_Otentikasi(): #Program loop ke fungsi ini jika input salah
    print("""
        __________________________________________
        |                                        |
        |                                        |
        |                  LOGIN                 |
        |                                        |
        |  NOMOR REKENING ATAU KATA SANDI SALAH  |
        |             MOHON COBA LAGI            |
        |                                        |
        |                                        |
        |________________________________________|
        """)
    nomor_rekening = str(input("NOMOR REKENING: "))
    password = str(input("KATA SANDI: "))
    return [nomor_rekening, password]


def Main_Otentikasi(data_nasabah):
    #Mengambil data dari luar fungsi
   

    #Input inisial, Nomor Rekening dan password
    print( 
        """
        __________________________________________
        |                                        |
        |                                        |
        |                  LOGIN                 |
        |                                        |
        |       MASUKKAN NOMOR REKENING DAN      |
        |                KATA SANDI              |
        |                                        |
        |                                        |
        |________________________________________|
        """)
    nomor_rekening = str(input("NOMOR REKENING: "))
    password = str(input("KATA SANDI: "))
    data_nasabah_online = {} #Informasi nasabah kosong

    while not Otentikasi(nomor_rekening, password, data_nasabah): # Ketika found =false, loop balik ke autentikasi
        nomor_rekening, password = Salah_Otentikasi()

    for item in data_nasabah: #Menginput data nasabah ke sesi utama
        if nomor_rekening == item["nomor_rekening"]:
            data_nasabah_online = item

    return data_nasabah_online #Jika autentikasi benar, memberikan informasi tentang nasabah yang sedang melakukan transaksi


# Main program
