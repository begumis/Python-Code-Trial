isim = input("İsminizi giriniz: ")
soy_isim = input("Soy isminizi giriniz: ")
hobi= input("Hobilerinizi giriniz: ")
felsefe = input("Hayat felsefeniz var ise giriniz: ")

ekrana_basılacak_yazı = """ 
İsim            : {}
Soy isim        : {}
Hobileri        : {}
Hayat Felsefesi : {}
""".format(isim,soy_isim,hobi,felsefe)

print(ekrana_basılacak_yazı)