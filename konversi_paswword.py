file = open("password.txt",'w+')
password = input("Masukkan Angka : ")

print("1. Hexadecimal")
print("2. Oktal")
print("3. Biner")
print("Mau diubah menjadi apa : ")
choice = int(input("Masukkan Pilihan : "))

if choice == 1 :
    konversi = int(password, 16)
    print("Sudah berhasil")
elif choice == 2 :
    konversi = int(password, 8)
    print("Sudah berhasil")
elif choice == 3 :
    konversi = int(password,2)
    print("Sudah berhasil")
else :
    print("Pilihan tidak ditemukan")

file.write(str(konversi))
file.close()