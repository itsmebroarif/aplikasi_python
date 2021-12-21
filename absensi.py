class RPL:
    def __init__(self, nama, no_abs):
        self.nama = str(nama)
        self.absen = str(no_abs)
    def getNama(self):
        return self.nama
    def getAbsen(self):
        return self.absen
    def setNama(self, nama):
        self.nama = nama
    def setAbsen(self, no_abs):
        self.absen = no_abs

Daftar_karyawan = {}
loop = True

print("===================================================================")
print("             Selamat Datang Di Aplikasi Pendaftaran karyawan Baru     ")
print("===================================================================")
print("                                     Menu              ")
print("1. Tambah Data       ")
print("2. Hapus Data        ")
print("3. Tampilkan Data    ")
print("4. Cari karyawan        ")
print("5. Edit Nama karyawan   ")
print("6. Edit Nomor karyawan  ")
print("7. Jumlah Total karyawan yang Sudah Mendaftar")
print("0. Keluar            ")
print("======================================================================")

while loop:
    print("\n\n")
    menu = input("Masukan Menu : ")

    if menu == "1":
        nama = input("Masukan Nama : ")
        absen = input("Masukan No Absens : ")
        karyawan = RPL(nama, absen)
        Daftar_karyawan[absen] = karyawan
    elif menu == "2":
        input("Masukan Nomer Absen karyawan : ")
        if (absen in Daftar_karyawan):
            del Daftar_karyawan[absen]
        else:
            print("Data Tidak Ditemukan")
    elif menu == "3":
        for i in Daftar_karyawan:
            print("Nama karyawan : ", Daftar_karyawan[i].getNama())
            print("No Absen : ", Daftar_karyawan[i].getAbsen())
    elif menu == "4":
        absen = input("Masukan Nomor Absen karyawan : ")
        if absen in Daftar_karyawan:
            print("Nama karyawan : ", Daftar_karyawan[absen].getNama())
            print("Nomor Absen : ", Daftar_karyawan[absen].getAbsen())
        else:
            print("Data Tidak Ditemukan")
    elif menu == "5":
        absen = input("Masukan Nomor Absen karyawan : ")
        if absen in Daftar_karyawan:
            namaBaru = input("Masukan Nama Baru : ")
            Daftar_karyawan[absen].setNama(namaBaru)
        else:
            print("Data Tidak Ditemukan")
    elif menu == "6":
        absen = input("Masukan Nomor Absen Baru : ")
        if absen in Daftar_karyawan:
            absenBaru = input("Masukan Nomor Absen Baru : ")
            Daftar_karyawan[absen].setAbsen()
        else:
            print("Data Tidak Ditemukan")
    elif menu == "7":
        print("Jumlah Total karyawan: ", len(Daftar_karyawan))
    elif menu == "0":
        loop = False
    else:
        print("Command not Found ")