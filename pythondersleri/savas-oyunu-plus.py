import random
import os

class Hedef():
    def __init__(self):
        self.saglik = random.randint(5,10)
        self.güc = random.randint(3,8)
        self.kalkan =random.randint(1,6)
        self.yasiyor_mu = True
    def vur(self,oyuncu):
        atak = self.güc- oyuncu.kalkan
        oyuncu.saglik -=atak
        if oyuncu.saglik<=0:
            oyuncu.yasiyor_mu =False


class Oyuncu():
    def __init__(self):
        self.saglik = 40
        self.güc = 7
        self.kalkan = 2
        self.yasiyor_mu = True
    def vur(self,hedeff):
        atak = self.güc- hedeff.kalkan
        hedeff.saglik -=atak
        if hedeff.saglik<=0:
            hedeff.yasiyor_mu =False
            hedef.remove(hedeff)


hedef = list()
for a in range(5):
    hedef.append(Hedef())
oyuncu =Oyuncu()


while True:
    os.system("cls")
    print("Oyuncu  ------  Sağlık Değeri : {}  ------  Saldırı Değeri : {}  ------  Kalkan Değeri : {}".format(oyuncu.saglik,oyuncu.güc,oyuncu.kalkan))
    print("-"*90)
    for a in hedef:
        print("{}. Hedef  ------  Sağlık Değeri : {}  ------  Saldırı Değeri : {}  ------  Kalkan Değeri : {}".format(hedef.index(a)+1,a.saglik,a.güc, a.kalkan))
    if oyuncu.yasiyor_mu == False:
        print("Kaybettiniz")
        quit()
    elif not hedef:
        print("Kazandınız")

    try:
        secim = int(input("Hedef seçin : "))
        vurulan_hedef = hedef[secim-1]
        oyuncu.vur(vurulan_hedef)
        if hedef:
            saldırgan = hedef[random.randint(0,len(hedef)-1)]
            print("{}. Hedef  ------  Sağlık Değeri : {}  ------  Saldırı Değeri : {}  ------  Kalkan Değeri : {}".format(hedef.index(saldırgan) + 1, saldırgan.saglik, saldırgan.güc, saldırgan.kalkan))
            saldırgan.vur(oyuncu)
            input("Yeniden saldırmak için Enter'a basınız")
    except IndexError:
        input("Hatalı seçim yaptınız. Yeniden başlamak için Entar'a basınız")