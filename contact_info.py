list_contact = { "andi setiawan" : [ "andi setiawan","21","08909080801","Bermain Bola" ],
                 "andi hermawan" : [ "andi hermawan","21","08123456789","Bermain Basket, Bernyanyi"] }

while True :
    count = 1
    print("============ List Contact ============")
    for key,value in list_contact.items() :
        print( str(count) + ".\t" + value[0].title() )
        print( "\t" + "Usia : " + value[1] )
        print("\t" + "Nomor Telepon : " + value[2])
        print("\t" + "Hobby : " + value[3])
        count = count + 1
        print()

    print("Menu Pilihan")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Keluar")

    pilihan = int(input("Masukkan Pilihan : "))

    if pilihan == 1 :
        temp_list = []
        name = input("Nama : ")
        temp_list.append(name)

        umur = input("Umur : ")
        temp_list.append(umur)

        nomor = input("Nomor : ")
        temp_list.append(nomor)

        temp_hobby = ""
        count_hobby = int(input("Masukkan Jumlah Hobby : "))

        if count_hobby <= 1 and count_hobby > -1 :
            if count_hobby == 0 :
                temp_hobby = " - "
            else :
                hobby = input("Hobby : ")
                temp_hobby = hobby
        elif count_hobby > 1 :
            for i in range ( 0 , count_hobby, 1 ) :
                hobby = input("Hobby : ")

                if i+1 != count_hobby :
                    temp_hobby = temp_hobby + hobby.title() +", "
                else :
                    temp_hobby = temp_hobby + hobby.title()

        temp_list.append(temp_hobby)

        list_contact[name.lower()] = temp_list

    elif pilihan == 2 :
        try :
            delete = input("Masukkan Kontak : ")
            del list_contact[delete.lower()]
            print( "Kontak bernama " + delete.title() + " Berhasil dihapus" )
        except :
            print( "Nama Tidak Ditemukan " )
    elif pilihan == 3 :
        print("Program Selesai")
        break
    else :
        print( "Input tidak sesuai" )

