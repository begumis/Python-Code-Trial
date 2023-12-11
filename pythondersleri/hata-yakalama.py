#a = input("Bölünen: ")
#b = input("Bölen: ") #int ya da float almıyoruz çünkü value error verir
                     #sadece try daki ifade kontrol edilir.

try:
    a = input("Bölünen: ")  #inputlar mutlaka try da olmalı
    b = (input("Bölen: "))
    print("Sonuç = ", float(a)/float(b))
except ValueError:
    print("Lütfen geçerli bir sayı giriniz.")
except ZeroDivisionError:
    print("Bölen 0 olursa tanımsızdır.")