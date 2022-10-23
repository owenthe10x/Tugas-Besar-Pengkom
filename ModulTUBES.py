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
    nama = input("Masukkan nama lengkap\t:\t")
    no = input("Masukkan No KTP/NIK\t:\t")
    rek = input("Masukkan nomor rekening\t:\t")
    id = input("Masukkan user ID (tanpa spasi)\t:\t")
    password = input("Masukkan password\t:\t")
    pin = input("Masukkan pin\t(6 digit):\t")
    no_hp = input("Masukkan nomor handphone\t:\t")
    with open("data_pengguna.txt", mode="a") as fread:
        fread.write(
            f"{id}#{password}#{no}#{rek}#{pin}#{no_hp}#100000#{nama}\n")
    print("Pendaftaran akun berhasil!")
    system('pause')
    masuk()


def cari(id):
    with open("data_pengguna.txt", mode="r") as fread:
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
        pin = input("Masukkan pin anda\t:\t")
        with open("data_pengguna.txt", mode="r") as fread:
            for line in fread:
                if(line.split("#")[0] == id):
                    found = True
                    break
        templist = line.split("#")
        if(pin == templist[4]):
            status = True
            print("Pin benar!")
            break
        else:
            print("Pin salah!")
        tries += 1
    system('pause')
    return status


def operasi_saldo(id, nominal):
    baris = 0
    status = False
    with open("data_pengguna.txt", mode="r") as fread:
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
        with open("data_pengguna.txt", mode="w") as fwrite:
            fwrite.writelines(get_all)
        status = True
    else:
        print("Saldo anda tidak mencukupi!")
    return(status)


def masuk():
    system('cls')
    found = False
    global id
    tries = 0
    id = input("User ID\t\t: ")
    with open("data_pengguna.txt", mode="r") as fread:
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
                print("Login Berhasil!")
                system('pause')
                menu()
            else:
                print("Password salah!")
    pilihan = input("Ganti password? (y/n) ")
    if(pilihan.upper() == "Y"):
        ubah_password()
    else:
        masuk()


def ubah_password():
    system('cls')
    id = input("Masukkan user ID: ")
    lama = input("Masukkan password sekarang\t: ")
    baru = input("Masukkan password baru\t: ")
    ulang = input("Ulangi password baru\t: ")
    baris = 0
    with open("data_pengguna.txt", mode="r") as fread:
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
        with open("data_pengguna.txt", mode="w") as fwrite:
            fwrite.writelines(get_all)
        print("Password berhasil diubah!")
    else:
        print("Password yang anda ulangi salah!")
        system('pause')


def profil():
    system('cls')
    global id
    print("1. Informasi Akun")
    print("2. Ubah Password")
    pilihan = int(input("Pilihan: "))
    if(pilihan == 1):
        system('cls')
        data = cari(id)
        print(f"User ID\t: {data[0]}")
        print(f"Nama Pengguna\t: {data[7]}", end="")
        print(f"Nomor Rekening\t: {data[3]}")
        print(f"Nomor telepon\t: {data[5]}")
        print(f"Saldo\t: {data[6]}")
        system('pause')
        menu()
    elif(pilihan == 2):
        ubah_password()
    else:
        print("Masukkan 1 atau 2!")
        system('pause')
        profil()


def print_daftar(dictionary):
    print("Daftar instansi:")
    for i in dictionary:
        print(f"{i}")


def transfer():
    system('cls')
    print("Selamat datang di bagian transfer")
    print("Pastikan nomor rekening yang anda masukkan benar!")
    bank = input("Apakah anda ingin transaksi antarbank? (y/n)\n")
    if(bank.upper() == "Y"):
        print_daftar(daftar_instansi)
        instansi = input("Bank tujuan\t: ")
        kode = daftar_instansi.get(instansi.upper())
        if(kode == None):
            print("Instansi tidak tersedia.")
            system('pause')
            transfer()
        print(f"Kode bank adalah {kode}")
        tujuan = input(
            "Masukkan rekening tujuan (diawali dengan kode bank)\t: ")
        nominal = int(input("Masukkan nominal\t: "))
        catatan = input("Catatan\t: ")
        pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n) ")
        if(pilihan.upper() == "Y"):
            system('cls')
            bisa = check_pin()
            if(bisa):
                if(operasi_saldo(id, nominal)):
                    system('cls')
                    print("-" * 70)
                    print('|{:^70}|'.format("STRUK TRANSFER"))
                    print("-" * 70)
                    print('|{:<70}|'.format("TRANSFER BERHASIL!"))
                    print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
                    print('|{:<15}{:<55}|'.format("Tujuan", f": {tujuan}"))
                    nominal = ('{0:,}'.format(nominal).replace(',', '.'))
                    print('|{:<15}{:<55}|'.format(
                        "Nominal", f": Rp{nominal},00"))
                    print('|{:<15}{:<55}|'.format("Catatan", f": {catatan}"))
                    print("-" * 70)
                    print('|{:^70}|'.format("BANK RAKYAT ELITE"))
                    print("-" * 70)
                    system('pause')
                    menu()
            else:
                print(
                    "PIN yang anda masukkan sudah salah sebanyak 3x, silahkan mengulang!")
                system('pause')
                transfer()
        elif(pilihan.upper() == "N"):
            transfer()
        else:
            print("Masukkan y atau n!")
            system('pause')
            transfer()
    elif(bank.upper() == "N"):
        tujuan = input("Masukkan rekening tujuan\t: ")
        nominal = int(input("Masukkan nominal\t: "))
        catatan = input("Catatan\t: ")
        pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n) ")
        if(pilihan.upper() == "Y"):
            bisa = check_pin()
            if(bisa and operasi_saldo(id, nominal)):
                baris = 0
                with open("data_pengguna.txt", mode="r") as fread:
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
                with open("data_pengguna.txt", mode="w") as fwrite:
                    fwrite.writelines(get_all)
                with open("data_pengguna.txt", mode="r") as fread:
                    for line in fread:
                        if(line.split("#")[3] == tujuan):
                            temp = line.split("#")
                            break
                system('cls')
                print("-" * 70)
                print('|{:^70}|'.format("STRUK TRANSFER"))
                print("-" * 70)
                print('|{:<70}|'.format("TRANSFER BERHASIL!"))
                print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
                print('|{:<15}{:<55}|'.format("Tujuan", f": {tujuan}"))
                print('|{:<15}{:<55}|'.format(
                    "Nama Penerima", f": {temp[7]}", end=""))
                nominal = ('{0:,}'.format(nominal).replace(',', '.'))
                print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
                print('|{:<15}{:<55}|'.format("Catatan", f": {catatan}"))
                print("-" * 70)
                print('|{:^70}|'.format("BANK RAKYAT ELITE"))
                print("-" * 70)
                system('pause')
                menu()
            else:
                print(
                    "PIN yang anda masukkan sudah salah sebanyak 3x, silahkan mengulang!")
                system('pause')
                transfer()
        elif(pilihan.upper() == "N"):
            transfer()
        else:
            print("Masukkan y atau n!")
            system('pause')
            transfer()
    else:
        print("Masukkan y atau n!")
        system('pause')
        transfer()


def multi():
    global id
    system('cls')
    print("Selamat datang di bagian multi-payment")
    print("Pastikan kode pembayaran yang anda masukkan benar!")
    print_daftar(daftar_multipayment)
    data = cari(id)
    nama = input("Masukkan nama instansi/perusahaan\t: ")
    kode = daftar_multipayment.get(nama.upper())
    if(kode == None):
        print("Instansi tidak tersedia.")
        system('pause')
        multi()
    print(f"Kode perusahaannya adalah {kode}")
    bayar = input(
        "Masukkan kode pembayaran (diawali dengan kode perusahaan)\t: ")
    nominal = int(input("Masukkan nominal\t: "))
    check_pin()
    pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n)")
    if(pilihan.upper() == "Y"):
        if(operasi_saldo(id, nominal)):
            system('cls')
            print("-" * 70)
            print('|{:^70}|'.format("STRUK PEMBAYARAN"))
            print("-" * 70)
            print('|{:<70}|'.format("PEMBAYARAN BERHASIL!"))
            print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
            print('|{:<15}{:<55}|'.format("Kode Referensi", f": {bayar}"))
            print('|{:<15}{:<55}|'.format("Instansi", f": {nama.upper()}"))
            nominal = ('{0:,}'.format(nominal).replace(',', '.'))
            print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
            print("-" * 70)
            print('|{:^70}|'.format("BANK RAKYAT ELITE"))
            print("-" * 70)
            system('pause')
    elif(pilihan.upper() == "N"):
        multi()
    else:
        print("Masukkan y atau n!")
        system('pause')
        multi()
    menu()


def topup():
    system('cls')
    global id
    print("Selamat datang di bagian top-up")
    print("Pastikan nomor akun yang anda masukkan benar!")
    print_daftar(daftar_topup)
    data = cari(id)
    nama = input("Masukkan penyedia jasa\t:\t")
    kode = daftar_topup.get(nama.upper())
    if(kode == None):
        print("Instansi tidak tersedia.")
        system('pause')
        topup()
    print(f"Kode penyedia jasa adalah {kode}")
    bayar = input(
        "Masukkan kode top-up (diakhiri dengan kode penyedia jasa)\t: ")
    nominal = int(input("Masukkan nominal top-up\t: "))
    check_pin()
    pilihan = input("Apakah data yang anda masukkan sudah benar? (y/n)")
    if(pilihan.upper() == "Y"):
        if(operasi_saldo(id, nominal)):
            system('cls')
            operasi_saldo(id, nominal)
            print("-" * 70)
            print('|{:^70}|'.format("STRUK TRANSFER"))
            print("-" * 70)
            print('|{:<70}|'.format("TRANSFER BERHASIL!"))
            print('|{:<15}{:<55}|'.format("Waktu", f": {waktu()}"))
            print('|{:<15}{:<55}|'.format(
                "Tujuan", f": {bayar[0:(len(bayar)-4)]}"))
            print('|{:<15}{:<55}|'.format("Instansi", f": {nama.upper()}"))
            print('|{:<15}{:<55}|'.format(
                "Nama Penerima", f": {data[7]}", end=""))
            nominal = ('{0:,}'.format(nominal).replace(',', '.'))
            print('|{:<15}{:<55}|'.format("Nominal", f": Rp{nominal},00"))
            print("-" * 70)
            print('|{:^70}|'.format("BANK RAKYAT ELITE"))
            print("-" * 70)
            system('pause')
    elif(pilihan.upper() == "N"):
        topup()
    else:
        print("Masukkan y atau n!")
        system('pause')
        topup()
    menu()


def kontak():
    system('cls')
    print("Frequently Asked Question")
    print("Q\t:\t\"Apa itu layanan BRE Mobile?\"")
    print("A\t:\tLayanan BRE Mobile adalah layanan perbankan dari BRE yang memberikan kemudahan dan kenyamanan dalam bertransaksi melalui smartphone.")
    print("Q\t:\t\"Apakah pembukaan rekening baru dapat dilakukan melalui aplikasi BRE Mobile?\"")
    print("A\t:\tPembukaan rekening baru tidak dapat dilakukan pada aplikasi BRE Mobile, melainkan harus mendatangi kantor cabang terdekat.")
    print("Q\t:\t\"Bagaimana cara mengubah password?\"")
    print("A\t:\tAnda dapat mengubah password pada menu profil lalu pilih menu ubah password.")
    print("Q\t:\t\"Bagaimana jika saya ingin melihat histori transaksi saya?\"")
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
    menu()


def menu():
    system('cls')
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
    elif(opsi == "4" or opsi.upper() == "TOP UP"):
        topup()
    elif(opsi == "5" or opsi.upper() == "FAQ DAN KONTAK"):
        kontak()
    elif(opsi == "6" or opsi.upper() == "LOG OUT"):
        print(
            "Terima kasih telah menggunakan layanan BRE Mobile, semoga hari anda menyenangkan!")
        system('pause')
        system('cls')
        exit()
    else:
        print("Masukkan opsi yang benar! (1-6)")
        menu()
        system('pause')
