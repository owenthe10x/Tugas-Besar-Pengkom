# bismillah selesai tepat waktu
from os import system
import datetime as dt
from ModulTUBES import *


while(1 > 0):
    print("""
██████╗ ██████╗ ███████╗    ███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗
██╔══██╗██╔══██╗██╔════╝    ████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝
██████╔╝██████╔╝█████╗      ██╔████╔██║██║   ██║██████╔╝██║██║     █████╗
██╔══██╗██╔══██╗██╔══╝      ██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝
██████╔╝██║  ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝""")
    print("-"*75)
    print("Masuk/Daftar/Keluar")
    opsi_awal = input("")
    if(opsi_awal.upper() == "MASUK"):
        masuk()
    elif(opsi_awal.upper() == "DAFTAR"):
        buat_akun()
    elif(opsi_awal.upper() == "KELUAR"):
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
        print("Pilihannya hanya Masuk/Daftar/Keluar !!!")
        system('pause')
        system('cls')

input("Press ENTER to exit")
