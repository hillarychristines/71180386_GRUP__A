# Hillary Christine S 71180386
# Universitas Kristen Duta Wacana


'''Soal Perulangan
Dalam suatu acara malam keakraban, Dion mempunyai ide untuk membuat sebuah permainan tebak angka. Inti dari permainan tersebut adalah setiap orang akan berusaha menebak angka yang sesungguhnya, jika tebakan belum tepat, maka orang selanjutnya akan menebak lagi. Begitu seterusnya hingga akhirnya angka yang sesungguhnya berhasil ditebak.
Sebagai teman yang baik, akhirnya kamu memutuskan untuk membantu Dion membuat program tersebut
'''

# Input
#  inputan -> int 1-10

# Proses
    # generate random number 
    # while tebakan!=angkaRandom:
    #       input lagi (tebak lagi)
    
# Output
    # print(Selamat anda berhasil menebak angka tersebut)

# Source code
# Input
import random
tebakan = 0
angkaRandom = random.randint(1, 10)
counter = 0

# Proses
while tebakan!=angkaRandom:
    tebakan = int(input("Tebak angka yang disembunyikan (1-10): "))
    counter += 1

# Output
print("Selamat Anda berhasil menebak angka yang disembunyikan yaitu %d dalam %d percobaan" %(angkaRandom, counter))