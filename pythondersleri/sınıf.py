class karakter():
    saglik = 0
    saldırı = 0
    silah = ""
    ekipman = ""
    isim = ""
    cephanelik = 0

savasci = karakter()
savasci.saglik = 250
savasci.silah = "Kılıç"
savasci.ekipman ="Kalkan"
savasci.isim = "Battal"
savasci.saldırı = 50

büyücü = karakter()
büyücü.isim ="Ahmet"
büyücü.saglik= 500
büyücü.silah ="Asa"
büyücü.ekipman="Pelerin"
büyücü.cephanelik=1200
büyücü.saldırı =25

savasci.saglik=savasci.saglik-büyücü.saldırı
print(savasci.saglik)