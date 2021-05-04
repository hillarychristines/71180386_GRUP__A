tuple_kontak = (
    "Hillary Christine",
    "Asri Meliana",
    "Annabela Ciaobella",
    "Syahrini Maharaini"
)

while True :
    print(" ********** Menu Pilihan ********** ")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Update Kontak")
    print("4. Tampil Kontak")
    print("5. Keluar / Exit")

    pilihan = int(input("Masukkan pilihan : "))

    if pilihan == 1 :
        tambah = input("Masukkan Nama yang akan ditambahkan : ")
        temp_tupple = list(tuple_kontak)
        temp_tupple.append(tambah)
        tuple_kontak = tuple(temp_tupple)
        print("Data berhasil ditambahkan")

    elif pilihan == 2 :
        indeks = int(input("Masukkan indeks : "))
        indeks = indeks - 1

        if len(tuple_kontak) < indeks :
            print("Data Tidak Ada")
        else :
            print("Data sekarang pada " + str(indeks + 1) + " adalah " + tuple_kontak[indeks])
            temp_tupple = list(tuple_kontak)
            print( "Data dengan nama " + temp_tupple.pop(indeks) + " telah berhasil di hapus" )
            tuple_kontak = tuple(temp_tupple)

    elif pilihan == 3 :
        indeks = int(input("Masukkan indeks : "))
        indeks = indeks - 1

        if len(tuple_kontak) < indeks :
            print("Data Tidak Ditemukan")
        else :
            print("Data sekarang pada " + str(indeks+1) + " adalah " + tuple_kontak[indeks])
            update = input("Ganti denan : ")
            temp_tupple = list(tuple_kontak)
            temp_tupple[indeks] = update
            tuple_kontak = tuple(temp_tupple)
            print("Sukses Data berhasil di Update !!!")

    elif pilihan == 4 :

        print()
        if len(tuple_kontak) == 0 :
            print("Tidak Ada Data")
        else :
            print("+++++++++++++++Daftar Kontak++++++++++++++++++")
            for i in range (len(tuple_kontak)) :
                print( str(i+1) + ". " + tuple_kontak[i] )
            print()

    elif pilihan == 5 :
        print("Program Berhenti")
        break
    else :
        print("Pilihan Tidak Ditemukan")