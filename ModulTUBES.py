from os import system
from platform import system_alias
from tabnanny import check
import datetime as dt

class akun:
    def __init__(acc, id, password):
        acc.id = id
        acc.password = password

def buat_akun(data_akun, data_pengguna):
    system('cls')
    nama = input("Masukkan nama lengkap\t:\t")
    no = int(input("Masukkan No KTP/NIK\t:\t"))
    rek = int(input("Masukkan nomor rekening\t:\t"))
    id = input("Masukkan user ID\t:\t")
    password = input("Masukkan password\t:\t")
    pin = int(input"Masukkan pin\t: \t)
    no_hp = int(input("Masukkan nomor handphone\t:\t"))
    print("Pendaftaran akun berhasil!")


def check_pin(data_pengguna):
    while(try <= 3):
        pin = int("Masukkan pin anda\t:\t")
        if(pin benar):
            print("Pin benar!")
        else:
            print("Pin salah!")
        try += 1


def ganti_pass(data_akun):
    system('cls'):
    id = input("User ID\t:\t")
    try = 1
    while(try <= 3):
        pin = int(input("PIN\t:\t"))
        if(pass ada di database):
            pass_baru = input("Password baru\t:\t")
        else:
            print("PIN SALAH!")
            try += 1


def masuk(data_akun):
    system('cls')
    id = input("User ID\t:\t")
    while(try <= 3):
        password = input("Password\t:\t")
        if(id ada di database):
            if(data_akun[id] == password):
                print("Login Berhasil!")
                system('pause')
            else:
                print("Password salah!")
        try += 1
    menu()


def ubah_password(data_akun):
    system('cls')
    id = input("Masukkan user ID: ")
    lama = input("Masukkan password sekarang: ")
    baru = input("Masukkan password baru: ")
    ulang = input("Ulangi password baru: ")
    if(baru == ulang):
        data_akun[id] = baru
    else:
        print("Password yang anda ulangi salah!")
        system('pause')
        data_akun()


def profil():
    print("1. Informasi Akun")
    print("2. Ubah Password")
    pilihan = int(input("Pilihan: "))
    if(pilihan == 1):
        print("User ID\t:\t")
        print("Nama Pengguna\t:\t")
        print("Nomor Rekening\t:\t")
        print("Saldo\t:\t")
    elif(pilihan == 2):
        ubah_password()


def transfer():
    system('cls')
    print("Selamat datang di bagian transfer")
    print("Pastikan nomor rekening yang anda masukkan benar!")
    tujuan = int(print("Masukkan rekening tujuan\t:\t"))
    nominal = int(print("Masukkan nominal\t:\t"))
    catatan = print("Catatan\t:\t")
    check_pin(data_pengguna)
    pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n)")
    if(pilihan.upper() == "Y"):
        system('cls')
        print("Receipt")
        print("Transfer BERHASIL!")
        print(dt)
        print(f"Tujuan: {tujuan}")
        print(f"A.n. {data_akun[tujuan]}")
        print(f"Rp {nominal}.00")
        print(f"Catatan: ")

    elif(pilihan.upper() == "N"):
        transfer()
    else:
        print("Masukkan y atau n!")
        system('pause')
        transfer()


def print_instansi(data_instansi):
    print("Daftar instansi:")


def multi(data_instansi):
    print("Selamat datang di bagian multi-payment")
    print("Pastikan kode pembayaran yang anda masukkan benar!")
    nama = input("Masukkan nama instansi/perusahaan\t:\t")
    kode = data_instansi[nama]
    print(f"Kode perusahaannya adalah {kode}")
    print("Masukkan kode pembayaran (diawali dengan kode perusahaan)\t:\t")
    check_pin(data_pengguna)
    pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n)")
    if(pilihan.upper() == "Y"):
        system('cls')
        print("Receipt")
    elif(pilihan.upper() == "N"):
        multi()
    else:
        print("Masukkan y atau n!")
        system('pause')
        multi()


def topup(data_jasa):
    system('cls')
    print("Selamat datang di bagian top-up")
    print("Pastikan nomor akun yang anda masukkan benar!")
    nama = input("Masukkan penyedia jasa\t:\t")
    kode = data_jasa[nama]
    print(f"Kode penyedia jasa adalah {kode}")
    print("Masukkan kode top-up (diakhiri dengan kode penyedia jasa)\t:\t")
    check_pin(data_pengguna)
    pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n)")
    if(pilihan.upper() == "Y"):
        system('cls')
        print("Receipt")
    elif(pilihan.upper() == "N"):
        topup()
    else:
        print("Masukkan y atau n!")
        system('pause')
        topup()


def kontak():
    print("Frequently Asked Question")
    print("Q\t:\t\"Bagaimana membuat rekening?\"")
    print("A\t:\tPembuatan rekening tidak dapat dilakukan pada aplikasi ini, melainkan harus mendatangi kantor cabang terdekat")
    print("Q\t:\t\"Bagaimana cara mengubah password akun?\"")
    print("A\t:\tAnda dapat mengubah password pada menu profil lalu pilih menu ubah password.")
    print("\n\nKontak Bank Rakyat Elite")
    print("-"*20)
    print("Whatsapp\t:\t")
    print("Telegram\t:\t")
    print("Instagram\t:\t")
    print("Twitter\t:\t")
    print("No. telp\t:\t")
    system('pause')


def menu():
    print("1. Profil dan Informasi")
    print("2. Transfer")
    print("3. Multi-payment")
    print("4. Top up")
    print("5. FAQ dan Kontak")
    print("6. Log out")
    opsi = input("Pilihan menu: ")
    if(opsi == "1" or opsi.upper() == "PROFIL DAN INFORMASI"):
        profil()
    elif(opsi == "2" or opsi.upper() == "TRANSFER"):
        transfer()
    elif(opsi == "3" or opsi.upper() == "MULTI-PAYMENT"):
        multi()
    elif(opsi == "4"):
        topup()
    elif(opsi == "5"):
        kontak()
    elif(opsi == "6"):
        print(
            "Terima kasih telah menggunakan aplikasi kami, semoga hari anda menyenangkan!")
        exit()
    else:
        print("Masukkan opsi yang benar! (1-6)")
        menu()
