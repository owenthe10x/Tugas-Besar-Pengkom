from os import system
from platform import system_alias
from tabnanny import check
import datetime as dt

dict_instansi = {
    "BCA" : 789,
    "BRI" : 289,
    "BNI" : 299,
    "MANDIRI" : 348,
    "BTN" : 209,
    "PERMATA BANK" : 630,
    "BANK JAGO" : 207,
    "BJB" : 202,
    "CIMBNIAGA" : 393,
    "DANAMON" : 415,
    "BANK DKI" : 419,
    "HSBC" : 892,
    "ICBC" : 932,
    "BUKOPIN" : 216,
    "MAYBANK" : 352,
    "NOBU" : 451
}

dict_multipayment = {
    "PLN" : 2674,
    "TSEL" : 1052,
    "XL" : 1912,
    "INDOSAT" : 4591,
    "3 PRABAYAR" : 1621,
    "SHOPEE" : 1955,
    "NETFLIX" : 9642,
    "DISNEY HOTSTAR" : 4955,
    "VIDIO" : 2249,
    "HBO" : 8215,
    "VIU" : 2921,
    "IQIYI" : 6618,
    "WETV" : 7553,
    "MOLA TV" : 4752
}

dict_topup = {
    "HEYBRE" : 647,
    "SHOPEEPAY" : 809,
    "GOPAY" : 129,
    "OVO" : 902,
    "DANA" : 224,
    "DOKU" : 315,
    "SAKUKU" : 116
}

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
    pin = int(input("Masukkan pin\t: \t")
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
    print("Q\t:\t\"Apa itu layanan BRE Mobile?\"")
    print("A\t:\tLayanan BRE Mobile adalah layanan perbankan dari BNE yang memberikan kemudahan dan kenyamanan dalam bertransaksi melalui smartphone.")
    print("Q\t:\t\"Apakah pembukaan rekening baru dapat dilakukan melalui aplikasi BRE Mobile?\"")
    print("A\t:\tPembukaan rekening baru tidak dapat dilakukan pada aplikasi BRE Mobile, melainkan harus mendatangi kantor cabang terdekat.")
    print("Q\t:\t\"Bagaimana cara mengubah password?\"")
    print("A\t:\tAnda dapat mengubah password pada menu profil lalu pilih menu ubah password.")
    print("Q\t:\t\Bagaimana jika saya ingin melihat histori transaksi saya?\"")
    print("A\t:\tAnda dapat melihat histori transaksi pada menu info rekening lalu pilih mutasi rekening.")
    print("Q\t:\t\"Apa yang harus dilakukan jika kartu BRE Debit hilang?\"")
    print("A\t:\tHal yang pertama harus dilakukan adalah memblokir kartu yang hilang melalui call center atau cabang.")
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