sözlük = {"Siyah":"Kara", "Beyaz":"Ak","Anıt":"Abide", "Tane":"Adet", "Kırmızı":"Al"}

#giris = input("Kelime giriniz : ")
#print("Eş anlamlı kelimesi: ", sözlük.get(giris,"Aradığınız kelime bulunamadı!"))

for a in sözlük.items():
     print(a)

print("")

for b in sözlük.keys():
     print(b)

print("")

for c in sözlük.values():
     print(c)