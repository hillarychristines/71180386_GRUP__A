inputan = input("Kalimat : ")

for any_word in inputan :
    if any_word == ' ' :
        print('_',end ="")
    else :
        print(any_word.lower(),end="")

