import random
import os

while True:

    os.system("cls")
    rastgele = random.randint(1,9)

    sayi = int(input("Bir sayı giriniz: "))
    print("Tuttuğum sayı :",rastgele)
    if sayi == rastgele:
        print("Tebrikler!!!")
        exit()
    else:
        input("Yeniden oynamak için enter'a basınız")

