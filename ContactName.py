set_contact = set()

while True :
    print(" = = = = = Daftar Pilihan = = = = = ")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Tampil Kontak")
    print("4 . Exit")

    pilihan = int(input("Pilihan : "))

    if pilihan == 1 :
        tambah = input("Data : ")

        if tambah not in set_contact :
            set_contact.add(tambah)
            print("Data bernama " + tambah + " berhasil ditambahkan")
        else :
            print("Data Sudah Ada")

    elif pilihan == 2 :

        if len(set_contact) == 0 :
            print("Data Kosong")
        else :
            hapus = int(input("Index ke : "))

            if hapus > len(set_contact) :
                print("Data Tidak Ditemukan")
            else :
                temp_list = list(set_contact)
                print("Data " + temp_list.pop(hapus-1) + " telah terhapus")
                set_contact = set(temp_list)

    elif pilihan == 3 :
        count = 1
        for data in set_contact :
            print(count,end=". ")
            print(data)
            count += 1

    elif pilihan == 4 :
        print("Terimakasih")
        break

    else :
        print("Input Tidak Ditemukan")