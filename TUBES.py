# bismillah selesai tepat waktu
from os import system
import datetime as dt
from ModulTUBES import menu, kontak


print("-"*50)
print("\t\t\tBANK RAKYAT ELITE MOBILE")
print("-"*50)
print("Masuk/Daftar/Keluar")

while(1 > 0):
    opsi_awal = input("")
    if(opsi_awal.upper() == "MASUK"):
        masuk()
    elif(opsi_awal.upper() == "DAFTAR"):
        buat_akun()
    elif(opsi_awal.upper() == "KELUAR"):
        exit()
    else:
        print("Pilihannya hanya Masuk/Daftar/Keluar !!!")
        system('pause')
        system('cls')

input("Press ENTER to exit")
