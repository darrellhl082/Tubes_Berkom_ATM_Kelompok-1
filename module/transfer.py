# Program Transfer ATM
# Memungkinkan nasabah untuk memindahkan uang dari satu rekening bank ke rekening bank lainnya

# KAMUS
# rekening_tujuan : array of dict
# norek : str
# pilih, nominal_transfer, konfirmasi : int

# ALGORITMA
from module import main_loop_config # mengambil kode dalam main_loop_config.py untuk variabel main_loop digunakan dalam program
min_saldo = 50000

def transfer(data_nasabah, nasabah_now):
    rekening_tujuan = dict()
    found = False
    status_transfer = False
  
        # validasi rekening tujuan
      
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
                rekening_tujuan = {}
                for item in data_nasabah:
                    # jika nomor rekening terdaftar, program akan menampilkan identitas nasabah untuk mengonfirmasi
                    if norek == item["nomor_rekening"] and norek != nasabah_now["nomor_rekening"]:
                        rekening_tujuan = item
                        norek_tujuan_text = f"NOMOR REKENING {item["nomor_rekening"]}".center(40)
                        nama_text = f"NAMA: {item["nama"]}".center(40)
                        found = True  
                if rekening_tujuan == {}:
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
    pilih = int(input())

    if pilih == 1: #Pilih benar
         while not status_transfer:
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

                print(
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
                """)
                konfirmasi = int(input())
                if konfirmasi == 1:
                    if nominal_transfer > nasabah_now["saldo"] or nasabah_now["saldo"] < min_saldo or nasabah_now["saldo"]-nominal_transfer < min_saldo:
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
                        status_transfer = True

                elif konfirmasi == 2:
                    # nge loop ulang ke input nominal transfer,tterus masukin ulang lagi
                    pass
                elif konfirmasi == 0:
                     status_transfer = 0
            
    elif pilih == 2:
        # nge loop ulang ke input norek, terus masukin ulang lagi
        pass
        
   

