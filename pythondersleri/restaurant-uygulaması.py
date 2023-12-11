masalar = dict()
for a in range(20):
    masalar[a]=0

def hesap_ekle():
    masa_no = int(input("Hesap eklenecek masayı giriniz: "))
    bakiye = masalar[masa_no]
    eklenecek_hesap = float(input("Eklenecek hesapı girin :"))
    güncel_bakiye = bakiye + eklenecek_hesap
    masalar[masa_no] = güncel_bakiye
    print("İşleminiz tamamlandı...")
def hesap_öde():
    masa_no = int(input("Hesabı ödenecek masayı giriniz: "))
    bakiye = masalar[masa_no]
    print("Masa {}'in hesabı {} Tl".format(masa_no,bakiye))
    masalar[masa_no] = 0
    print("Hesap ödendi...")
def dosya_kontrol(dosya_adı):
    try:
       dosya= open(dosya_adı,"r", encoding="utf-8")
       veri = dosya.read()
       veri =veri.split("\n")
       veri.pop()
       dosya.close()
       for a in enumerate(veri):
        masalar[a[0]] = float(a[1])
    except FileNotFoundError:
              dosya = open(dosya_adı,"w",encoding="utf-8")
              dosya.close()
              print("Kayıt dosyası oluşturuldu.")
def dosya_güncelle(dosya_adı):
    dosya = open(dosya_adı,"w",encoding="utf-8")
    for a in range(20):
        bakiye = masalar[a]
        bakiye =str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()

def ana_işlemler():
    dosya_kontrol("bakiye.txt")
    while True:
        print("""
            Battak KOÇ Restaurant Uygulaması
            
        1)Masaları Görüntüle
        2)Hesap Ekle
        3)Hesap Öde
        Q)Çıkış
         """)
        secim = input("Yapılacak işlemi giriniz: ")
        if secim =="1":
            for a in range(20):
                print("Masa {} için hesap: {} ".format(a,masalar[a]))
        elif secim == "2":
            hesap_ekle()
        elif secim == "3":
            hesap_öde()
        elif secim == "Q" or secim == "q":
            print("Çıkış yapılıyor... İyi günler...")
            quit()
        else:
            print("Hatalı seçim yaptınız... ")
        dosya_güncelle("bakiye.txt")
        input("Ana menüye dönmek için enter'a basınız. ")

ana_işlemler()