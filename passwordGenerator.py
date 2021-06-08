import re
infile = open('log_user.txt', 'w+')
tampung = ""

while True:
    username_input = input('Masukkan username : ')
    check = re.findall('[0-9]+',username_input)

    if check :
        total = 0
        for i in check :
            total += int(i)
        generate = oct(int(i))
        tampung += username_input+str(generate) + '\n'
    else :
        print("Username harus mengandung minimal 1 angka")

    user_continue = input('Y / N : ')

    if user_continue.lower() == 'n':
        break
    elif user_continue[0].lower() == 'n':
        break

    print(tampung)

infile.write(tampung)
print("File telah diperbaharui !")