# Program: Otentikasi identitas
# Spesifikasi: Mencari Username dan Password yang sesuai


# KAMUS
# Username: int; username pengguna
# Password: int; password pengguna
# i, : int
# found : bool; menentukan Username + Password sdh ditemukan/belum

# ALGORITMA
# Asumsi: input array sudah dibuat; N terdefinisi


def Otentikasi(Username, Password, data_nasabah):
    found = False  # found = False; X belum ditemukan
    i = 0
    while i < len(data_nasabah) and not found: #Akan berulang hingga semua dictionary nasabah diperiksa
        if data_nasabah[i]["nomor_rekening"] == Username and data_nasabah[i]["password"] == Password:
            found = True  # found = True; Username dan password benar
        else:
            i += 1  # hanya increment jika username atau password salah
    return found

def Salah_Otentikasi(): #Program loop ke fungsi ini jika input salah
    print("Nomor Rekening atau Password salah")
    print("Login ke akun masing-masing dengan menginput Nomor Rekening dan password")
    Username = str(input("Nomor Rekening: "))
    Password = str(input("Password: "))
    return [Username, Password]


def Main_Otentikasi(data_nasabah):
    #Mengambil data dari luar fungsi
   

    #Input inisial, Nomor Rekening dan Password
    print("Login ke akun masing-masing dengan menginput Nomor Rekening dan Password") 
    Username = str(input("Nomor Rekening: "))
    Password = str(input("Password: "))
    data_nasabah_online = {} #Informasi nasabah kosong

    while not Otentikasi(Username, Password, data_nasabah): # Ketika found =false, loop balik ke autentikasi
        Username, Password = Salah_Otentikasi()

    for item in data_nasabah: #Menginput data nasabah ke sesi utama
        if Username == item["nomor_rekening"]:
            data_nasabah_online = item

    return data_nasabah_online #Jika autentikasi benar, memberikan informasi tentang nasabah yang sedang melakukan transaksi


# Main program
