class Hayvan():
    def __init__(self,isim,yas,cins):
        self.isim = isim
        self.yas =yas
        self.cins = cins
    def Konusma(self):
      print("Hayvanlar konuşuyor")
class Köpek(Hayvan):
    def __init__(self,isim,yas,cins,sadiklik):
        super().__init__(isim,yas,cins)
        self.sadiklik = sadiklik
class Kedi (Hayvan):
    def __init__(self, isim, yas, cins, uyku_saati):
        super().__init__(isim, yas, cins)
        self.uyku_saati = uyku_saati

köpek = Köpek("Cesur", 2, "Kangal", 100)
print(köpek.isim,köpek.yas,köpek.cins,köpek.sadiklik)
kedi = Kedi("Tarçın", 2,"Tekir",15)
print(kedi.isim, kedi.yas, kedi.cins, kedi.uyku_saati)
köpek.Konusma()