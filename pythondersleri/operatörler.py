belirlenmis_kullanıcı_adı = "BattalKoç"
belirlenmis_sifre = "Python"

while True:
    kullanıcı_adı = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    if kullanıcı_adı != belirlenmis_kullanıcı_adı:
        print("Kullanıcı adınız hatalı!")
    elif sifre != belirlenmis_sifre:
        print("Şifreniz hatalı!")
    else:
        print("Giriş yaptınız!")
        exit()
