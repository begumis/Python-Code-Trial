import sqlite3
"""kisiselBilgiler= [
    ("Battal","Koç",30,"Ankara"),
    ("Ahmet","Yılmaz",45,"Kars"),
    ("Ayşe","Hikmet",13,"İstanbul")
]"""
db = sqlite3.connect("veritabani.db")
imlec = db.cursor()
"""imlec.execute("CREATE TABLE IF NOT EXISTS 'kisiselBilgiler'(isim,soyisim,yas,dyeri)")
for veri in kisiselBilgiler:
    imlec.execute("INSERT INTO 'kisiselBilgiler' VALUES (?,?,?,?)",veri)
db.commit()
"""
imlec.execute("SELECT * FROM 'kisiselBilgiler' ")
veriler = imlec.fetchall()
for a in veriler:
    print(a)
print("-"*90)

imlec.execute("SELECT isim,dyeri FROM 'kisiselBilgiler' ")
veriler2= imlec.fetchall()
for a in veriler2:
    print(a)
print("-"*90)

imlec.execute("SELECT * FROM 'kisiselBilgiler' WHERE dyeri='Kars' ")
veriler3= imlec.fetchall()
for a in veriler3:
    print(a)
print("-"*90)

imlec.execute("SELECT isim FROM 'kisiselBilgiler' WHERE dyeri='Kars' ")
veriler3= imlec.fetchall()
for a in veriler3:
    print(a)
print("-"*90)

db.close()