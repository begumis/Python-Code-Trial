rehber  = {
    "Battal": {
        "Cep":3456782321,
        "İş":1434569570,
        "Ev":8472785022,
    },
    "Ahmet": {
            "Cep":3456782321,
            "İş":1434569570,
            "Ev":8472785022,
        },
    "Mürşide": {
                "Cep":3456782321,
                "İş":1434569570,
                "Ev":8472785022,
            }
}

while True:
    isimler = rehber.keys()
    giris = input("Kişi adı: ")

    if giris in isimler:
        tel = input("İstediğiniz telefon numarası hangisidir? : ")
        print(rehber.get(giris).get(tel,"İstediğiniz numara mevcut değildir."))
    else:
        print("İstediğiniz kişi mevcut değildir.")

    cıkıs = input("Yeniden arama yapmak için enter'a basınız veya çıkış yapmak isterseniz Q tuşuna basıp enterlayın...")

    if cıkıs == "Q" or cıkıs == "q":
        print("ÇIKIŞ YAPILIYOR...")
        quit()


