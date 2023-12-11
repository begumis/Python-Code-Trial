"""dosya = open("deneme.txt","a",encoding="utf-8")
eklenecek_veri = "\nHayat Sevince Güzel."
dosya.write(eklenecek_veri)
dosya.close()"""

dosya = open("deneme.txt","r",encoding="utf-8")
veri = dosya.readlines()
print(veri)
del veri[0]
print(veri)
dosya.close()

dosya= open("deneme.txt", "w",encoding="utf-8")
for a in veri:
    dosya.write(a)

dosya.close()
