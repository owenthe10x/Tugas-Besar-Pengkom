from os import system
from platform import system_alias
from tabnanny import check
from datetime import datetime as dt

templist = []
id = ""

daftar_instansi = {
    "BCA": 789,
    "BRI": 289,
    "BNI": 299,
    "MANDIRI": 348,
    "BTN": 209,
    "PERMATA BANK": 630,
    "BANK JAGO": 207,
    "BJB": 202,
    "CIMBNIAGA": 393,
    "DANAMON": 415,
    "BANK DKI": 419,
    "HSBC": 892,
    "ICBC": 932,
    "BUKOPIN": 216,
    "MAYBANK": 352,
    "NOBU": 451
}

daftar_multipayment = {
    "PLN": 2674,
    "TSEL": 1052,
    "XL": 1912,
    "INDOSAT": 4591,
    "3 PRABAYAR": 1621,
    "SHOPEE": 1955,
    "NETFLIX": 9642,
    "DISNEY HOTSTAR": 4955,
    "VIDIO": 2249,
    "HBO": 8215,
    "VIU": 2921,
    "IQIYI": 6618,
    "WETV": 7553,
    "MOLA TV": 4752
}

daftar_topup = {
    "HEYBRE": 647,
    "SHOPEEPAY": 809,
    "GOPAY": 129,
    "OVO": 902,
    "DANA": 224,
    "DOKU": 315,
    "SAKUKU": 116
}


def waktu():
    now = dt.now()
    waktu = now.strftime("%d-%m-%y %H:%M:%S")
    return waktu


def buat_akun():
    print("-" * 101)
    print('|{:^100}|'.format("PENDAFTARAN AKUN BARU"))
    print("-" * 101)
    gaada = False
    nama = input("Masukkan nama lengkap\t\t\t: ")
    no = input("Masukkan No KTP/NIK\t\t\t: ")
    rek = input("Masukkan nomor rekening\t\t\t: ")
    id = input("Masukkan user ID (tanpa spasi)\t\t: ")
    with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
            for line in fread:
                if(line.split("#")[0] == id):
                    gaada = True
    while(gaada == True):
        print("User ID tidak tersedia!")
        system('pause')
        system('cls')
        print("-" * 101)
        print('|{:^100}|'.format("PENDAFTARAN AKUN BARU"))
        print("-" * 101)
        print(f"Masukkan nama lengkap\t\t\t: {nama}")
        print(f"Masukkan No KTP/NIK\t\t\t: {no}")
        print(f"Masukkan nomor rekening\t\t\t: {rek}")
        id = input("Masukkan user ID (tanpa spasi)\t\t: ")
        with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
            for line in fread:
                if(line.split("#")[0] == id):
                    gaada = True
                    break
                else:
                    gaada= False
            
    password = input("Masukkan password\t\t\t: ")
    pin = input("Masukkan pin (6 digit)\t\t\t: ")
    no_hp = input("Masukkan nomor handphone\t\t: ")     
    with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="a") as fwrite:
        fwrite.write(
            f"{id}#{password}#{no}#{rek}#{pin}#{no_hp}#100000#{nama}\n")
    print("Pendaftaran akun berhasil!")
    system('pause')
    masuk()


def cari(id):
    with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
        for line in fread:
            if(line.split("#")[0] == id):
                break
    templist = line.split("#")
    return templist


def check_pin():
    system('cls')
    status = False
    tries = 0
    while(tries < 3):
        global id
        pin = input("Masukkan PIN anda\t: ")
        with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
            for line in fread:
                if(line.split("#")[0] == id):
                    found = True
                    break
        templist = line.split("#")
        if(pin == templist[4]):
            status = True
            print("PIN benar!")
            break
        else:
            print("PIN salah!")
            system('pause')
            system('cls')
        tries += 1
    system('pause')
    return status


def operasi_saldo(id, nominal):
    baris = 0
    status = False
    with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
        for line in fread:
            if(id == line.split("#")[0]):
                temp = line.split("#")
                break
            baris += 1
        fread.seek(0)
        get_all = fread.readlines()
    if(int(temp[6]) >= nominal):
        temp[6] = int(temp[6])
        temp[6] -= nominal
        temp[6] = str(temp[6])
        get_all[baris] = "#".join(temp)
        with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="w") as fwrite:
            fwrite.writelines(get_all)
        status = True
    else:
        system('cls')
        print("Saldo anda tidak mencukupi!")
    return(status)


def masuk():
    system('cls')
    found = False
    global id
    tries = 0
    print("-" * 36)
    print('|{:^35}|'.format("MASUK"))
    print("-" * 36)
    id = input("User ID\t\t: ")
    with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
        for line in fread:
            if(line.split("#")[0] == id):
                found = True
                break
    if(found == False):
        print("Akun tidak ditemukan!")
        system('pause')
        masuk()
    else:
        while(tries < 3):
            tries += 1
            password = input("Password\t: ")
            templist_login = line.split("#")
            if(password == templist_login[1]):
                print("\n> Login Berhasil!")
                system('pause')
                menu()
            else:
                print("Password salah!")
                system('pause')
                system('cls')
                print("-" * 36)
                print('|{:^35}|'.format("MASUK"))
                print("-" * 36)
                print(f"User ID\t\t: {id}")
    pilihan = input("Ganti password? (y/n) ")
    if(pilihan.upper() == "Y"):
        ubah_password()
    else:
        masuk()


def ubah_password():
    system('cls')
    print("-" * 56)
    print('|{:^55}|'.format("UBAH PASSWORD"))
    print("-" * 56)
    id = input("Masukkan user ID\t\t: ")
    while True:
        lama = input("Masukkan password sekarang\t: ")
        with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
            for line in fread:
                if(line.split("#")[0] == id):
                    found = True
                    break
        if(lama != line.split("#")[1]):
            print("Password tidak sesuai!")
            system('pause')
            system('cls')
            print("-" * 56)
            print('|{:^55}|'.format("UBAH PASSWORD"))
            print("-" * 56)
            print(f"User ID\t\t\t\t: {id}")
            continue
        else:
            baru = input("Masukkan password baru\t\t: ")
            ulang = input("Ulangi password baru\t\t: ")
            baris = 0
            with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
                for line in fread:
                    if(id == line.split("#")[0]):
                        temp = line.split("#")
                        break
                    baris += 1
                fread.seek(0)
                get_all = fread.readlines()
            if(baru == ulang):
                temp[1] = baru
                get_all[baris] = "#".join(temp)
                with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="w") as fwrite:
                    fwrite.writelines(get_all)
                print("\nPassword berhasil diubah!")
                system('pause')
                masuk()
            else:
                print("Password yang anda ulangi salah!")
                system('pause')
                ubah_password()


def profil():
    system('cls')
    global id
    print("1. Informasi Akun")
    print("2. Ubah Password")
    pilihan = int(input("Pilihan: "))
    if(pilihan == 1):
        system('cls')
        data = cari(id)
        print("-" * 40) # sesuain sama  max input pas pendaftaran
        print('|{:^39}|'.format("INFORMASI AKUN"))
        print("-" * 40)
        print(f"User ID\t\t: {data[0]}")
        print(f"Nama Pengguna\t: {data[7]}", end="")
        print(f"Nomor Rekening\t: {data[3]}")
        print(f"Nomor telepon\t: {data[5]}")
        print(f"Saldo\t\t: {data[6]}")
        system('pause')
        menu()
    elif(pilihan == 2):
        ubah_password()
    else:
        print("Masukkan 1 atau 2!")
        system('pause')
        profil()


def print_daftar(dictionary):
    print("\nDaftar instansi:")
    print("-" * 16)
    for i in dictionary:
        print(f"{i}")


def transfer():
    system('cls')
    print("-" * 76)
    print('|{:^75}|'.format("TRANSFER"))
    print("-" * 76)
    bank = input("""Pilihan transfer:

1. Antarbank
2. Antarrekening
    
> Masukkan pilihan: """)
    if(bank == "1"):
        system('cls')
        print("-" * 76)
        print('|{:^75}|'.format("TRANSFER"))
        print("-" * 76)
        print_daftar(daftar_instansi)
        print("-" * 16)
        instansi = input("\nMasukkan nama bank tujuan\t\t\t\t: ")
        kode = daftar_instansi.get(instansi.upper())
        if(kode == None):
            print("Instansi tidak tersedia.")
            system('pause')
            transfer()
        print(f"Kode bank adalah \t\t\t\t\t: {kode}")
        tujuan = input(
            "Masukkan rekening tujuan (diawali dengan kode bank)\t: ")
        nominal = int(input("Masukkan nominal\t\t\t\t\t: "))
        catatan = input("Catatan (max 50 karakter)\t\t\t\t: ")
        print("\n")
        pilihan = input("""Mohon pastikan kembali data yang anda masukkan!
Data sudah benar?
1. Lanjut
2. Kembali
Masukkan pilihan: """)
        if(pilihan == "1"):
            system('cls')
            bisa = check_pin()
            if(bisa):
                if(operasi_saldo(id, nominal)):
                    system('cls')
                    print("-" * 71)
                    print('|{:^70}|'.format("STRUK TRANSFER"))
                    print("-" * 71)
                    print('|{:<70}|'.format("TRANSFER BERHASIL!"))
                    print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
                    print('|{:<15}{:<55}|'.format("Tujuan", f": {tujuan}"))
                    nominal = ('{0:,}'.format(nominal).replace(',', '.'))
                    print('|{:<15}{:<55}|'.format(
                        "Nominal", f": Rp{nominal},00"))
                    print('|{:<15}{:<55}|'.format("Catatan", f": {catatan}"))
                    print("-" * 71)
                    print('|{:^70}|'.format("BANK RAKYAT ELITE"))
                    print("-" * 71)
                    system('pause')
                    menu()
                else:
                    system('pause')
                    menu()
            else:
                print(
                    "PIN yang anda masukkan sudah salah sebanyak 3x, silahkan mengulang!")
                system('pause')
                transfer()
        elif(pilihan == "2"):
            transfer()
        else:
            print("Masukkan 1 atau 2!")
            system('pause')
            transfer()
    elif(bank == "2"):
        system('cls')
        print("-" * 76)
        print('|{:^75}|'.format("TRANSFER"))
        print("-" * 76)
        tujuan = input("Masukkan rekening tujuan\t: ")
        nominal = int(input("Masukkan nominal\t\t: "))
        catatan = input("Catatan (max 50 karakter)\t: ")
        pilihan = input("""
Mohon pastikan kembali data yang anda masukkan!
Data sudah benar?
1. Lanjut
2. Kembali
Masukkan pilihan: """)
        if(pilihan == "1"):
            bisa = check_pin()
            if(bisa and operasi_saldo(id, nominal)):
                baris = 0
                with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
                    for line in fread:
                        if(line.split("#")[3] == tujuan):
                            temp = line.split("#")
                            break
                        baris += 1
                    fread.seek(0)
                    get_all = fread.readlines()
                temp[6] = int(temp[6])
                temp[6] += nominal
                temp[6] = str(temp[6])
                get_all[baris] = "#".join(temp)
                with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="w") as fwrite:
                    fwrite.writelines(get_all)
                with open("C:/Users/PC/.vscode/python/chapter 00/TUBES1/data_pengguna.txt", mode="r") as fread:
                    for line in fread:
                        if(line.split("#")[3] == tujuan):
                            temp = line.split("#")
                            break
                system('cls')
                print("-" * 71)
                print('|{:^70}|'.format("STRUK TRANSFER"))
                print("-" * 71)
                print('|{:<70}|'.format("TRANSFER BERHASIL!"))
                print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
                print('|{:<15}{:<55}|'.format("Tujuan", f": {tujuan}"))
                print('|{:<15}{:<55}|'.format(
                    "Nama Penerima", f": {temp[7].strip()}"))
                nominal = ('{0:,}'.format(nominal).replace(',', '.'))
                print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
                print('|{:<15}{:<55}|'.format("Catatan", f": {catatan}"))
                print("-" * 71)
                print('|{:^70}|'.format("BANK RAKYAT ELITE"))
                print("-" * 71)
                system('pause')
                menu()
            elif(bisa and operasi_saldo(id, nominal) == False):
                system('pause')
                menu()
            else:
                print(
                    "PIN yang anda masukkan sudah salah sebanyak 3x, silahkan mengulang!")
                system('pause')
                transfer()
        elif(pilihan.upper() == "2"):
            transfer()
        else:
            print("Masukkan 1 atau 2!")
            system('pause')
            transfer()
    else:
        print("Masukkan 1 atau 2!")
        system('pause')
        transfer()


def multi():
    global id
    system('cls')
    print("-" * 76)
    print('|{:^75}|'.format("MULTIPAYMENT"))
    print("-" * 76)
    print_daftar(daftar_multipayment)
    print("-" * 16)
    data = cari(id)
    nama = input("\nMasukkan nama instansi/perusahaan\t\t\t: ")
    kode = daftar_multipayment.get(nama.upper())
    if(kode == None):
        print("Instansi tidak tersedia.")
        system('pause')
        multi()
    print(f"Kode perusahaan \t\t\t\t\t: {kode}")
    bayar = input(
        "Kode pembayaran (diawali dengan kode perusahaan)\t: ")
    nominal = int(input("Masukkan nominal\t\t\t\t\t: "))
    pilihan = input("""\n\nMohon pastikan kembali data yang anda masukkan!
Data sudah benar?
1. Lanjut
2. Kembali
Masukkan pilihan: """)
    if(pilihan.upper() == "1"):
        if(check_pin() == True):
            if(operasi_saldo(id, nominal)):
                system('cls')
                print("-" * 71)
                print('|{:^70}|'.format("STRUK PEMBAYARAN"))
                print("-" * 71)
                print('|{:<70}|'.format("PEMBAYARAN BERHASIL!"))
                print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
                print('|{:<15}{:<55}|'.format("Kode Referensi", f": {bayar}"))
                print('|{:<15}{:<55}|'.format("Instansi", f": {nama.upper()}"))
                nominal = ('{0:,}'.format(nominal).replace(',', '.'))
                print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
                print("-" * 71)
                print('|{:^70}|'.format("BANK RAKYAT ELITE"))
                print("-" * 71)
                system('pause')
            else:
                multi()
    elif(pilihan.upper() == "2"):
        multi()
    else:
        print("Masukkan 1 atau 2!")
        system('pause')
        multi()
    menu()


def topup():
    system('cls')
    global id
    print("-" * 76)
    print('|{:^75}|'.format("TOP-UP"))
    print("-" * 76)
    print_daftar(daftar_topup)
    print("-" * 16)
    data = cari(id)
    nama = input("\nMasukkan penyedia jasa\t\t\t\t: ")
    kode = daftar_topup.get(nama.upper())
    if(kode == None):
        print("Instansi tidak tersedia.")
        system('pause')
        topup()
    print(f"Kode penyedia jasa\t\t\t\t: {kode}")
    bayar = input(
        "Kode top-up (no. akun + kode penyedia jasa)\t: ")
    nominal = int(input("Masukkan nominal top-up\t\t\t\t: "))
    pilihan = input("""

Mohon pastikan kembali data yang anda masukkan!
Data sudah benar?
1. Lanjut
2. Kembali
Masukkan pilihan: """)
    check_pin()
    if(pilihan.upper() == "1"):
        if(operasi_saldo(id, nominal)):
            system('cls')
            operasi_saldo(id, nominal)
            print("-" * 71)
            print('|{:^70}|'.format("STRUK TRANSFER"))
            print("-" * 71)
            print('|{:<70}|'.format("TRANSFER BERHASIL!"))
            print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
            print('|{:<15}{:<55}|'.format(
                "Tujuan", f": {bayar[0:(len(bayar)-3)]}"))
            print('|{:<15}{:<55}|'.format("Instansi", f": {nama.upper()}"))
            print('|{:<15}{:<55}|'.format(
                "Nama Penerima", f": {data[7].strip()}"))
            nominal = ('{0:,}'.format(nominal).replace(',', '.'))
            print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
            print("-" * 71)
            print('|{:^70}|'.format("BANK RAKYAT ELITE"))
            print("-" * 71)
            system('pause')
        else:
            topup()
    elif(pilihan.upper() == "2"):
        topup()
    else:
        print("Masukkan 1 atau 2!")
        system('pause')
        topup()
    menu()


def kontak():
    system('cls')
    print("-" * 91)
    print('|{:^90}|'.format("FREQUENTLY ASKED QUESTIONS"))
    print("-" * 91)
    print("")
    print("Q\t: \"Apa itu layanan BRE Mobile?\"")
    print("""A\t: > Layanan BRE Mobile adalah layanan perbankan dari BRE yang memberikan
            kemudahan dan kenyamanan dalam bertransaksi melalui smartphone.\n""")
    print("Q\t: \"Apakah pembukaan rekening baru dapat dilakukan melalui aplikasi BRE Mobile?\"")
    print("""A\t: > Pembukaan rekening baru tidak dapat dilakukan pada aplikasi BRE Mobile, tetapi
            harus mendatangi kantor cabang terdekat.""")
    print("Q\t: \"Bagaimana cara mengubah password?\"")
    print("A\t: > Anda dapat mengubah password pada menu profil lalu pilih menu ubah password.\n")
    print("Q\t: \"Bagaimana jika saya ingin melihat histori transaksi saya?\"")
    print("""A\t: > Anda dapat melihat histori transaksi pada menu info rekening lalu pilih mutasi 
            rekening.\n""")
    print("Q\t: \"Apa yang harus dilakukan jika kartu BRE Debit hilang?\"")
    print("""A\t: > Hal yang pertama harus dilakukan adalah memblokir kartu yang hilang melalui 
            call center atau cabang.""")
    print("")
    print("-" * 91)
    print("\n")
    print("-" * 58)
    print('|{:^57}|'.format("KONTAK BANK RAKYAT ELITE"))
    print("-" * 58)
    print("")
    print("Whatsapp\t: 081321899777")
    print("Telegram\t: @siapbremobile")
    print("Instagram\t: @siapbremobile")
    print("Twitter\t\t: @siapbremobile")
    print("No. telp\t: 12120")
    print("E-mail\t\t: halobremobile@bre.co.id")
    print("")
    print("""Alamat\t\t:
(1) Jl. Bendungan Hilir No.21, Biruan, Kec. Setiaselalu,
    Kota Maykarta Selatan, Maykarta, 12920
(2) Jl. Ganesa No. 277, Cirusa, Kec. Istananangor, 
    Kota Bumina, Jawa Barat, 40411""")
    print("")
    print("-" * 58)
    system('pause')
    menu()


def menu():
    system('cls')
    print("-" * 31)
    print('|{:^30}|'.format("MENU"))
    print("-" * 31)
    print("")
    print("1. Profil dan Informasi")
    print("2. Transfer")
    print("3. Multipayment")
    print("4. Top-up")
    print("5. FAQ dan Kontak")
    print("6. Keluar")
    opsi = input("\n> Pilihan menu: ")
    if(opsi == "1" or opsi.upper() == "PROFIL DAN INFORMASI"):
        profil()
    elif(opsi == "2" or opsi.upper() == "TRANSFER"):
        transfer()
    elif(opsi == "3" or opsi.upper() == "MULTIPAYMENT"):
        multi()
    elif(opsi == "4" or opsi.upper() == "TOP-UP"):
        topup()
    elif(opsi == "5" or opsi.upper() == "FAQ DAN KONTAK"):
        kontak()
    elif(opsi == "6" or opsi.upper() == "KELUAR"):
        system('cls')
        print(
            "Terima kasih telah menggunakan layanan BRE Mobile, semoga hari anda menyenangkan!")
        print("-" * 95, end="")
        print("""
███████████████████████████████████████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─█─▄███▄─▄▄▀██▀▄─██▄─█─▄█▄─█─▄██▀▄─██─▄─▄─███▄─▄▄─█▄─▄███▄─▄█─▄─▄─█▄─▄▄─█
██─▄─▀██─▀─███─█▄▀─███─▄▀█████─▄─▄██─▀─███─▄▀███▄─▄███─▀─████─██████─▄█▀██─██▀██─████─████─▄█▀█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀""")
        print("-" * 95)
        system('pause')
        system('cls')
        exit()
    else:
        print("Masukkan opsi yang benar! (1-6)")
        menu()
        system('pause')
