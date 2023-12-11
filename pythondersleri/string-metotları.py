a = "Battal Koç Python Kursuİ"

print(a.replace("a", ""))
print(a.replace("İ","I"))

b ="""
Tarayıcı izolasyonu, bir internet kullanıcısının tarama etkinliğini (ve ilişkili siber riskleri) içinde bulunduğu yerel 
ağ ve altyapıdan fiziksel olarak yalıtmayı amaçlayan bir siber güvenlik modelidir.
 Tarayıcı izolasyon teknolojileri farklı yöntemlerle bu modeli gerçekleştirse de ortak amaç tarayıcı ve kullanıcı tarama
 etkinliğini efektif şekilde birbirinden izole ederek web-tarayıcıları, tarayıcı tabanlı güvenlik açıklarından ve internet
  kaynaklı fidye yazılımı ve benzer kötü amaçlı yazılımlardan korumaktır.[1] Uzaktan tarayıcı izolasyonu (Remote Browser
   Isolation, RBI) olarak bilinen modelde, teknoloji sağlayıcısı tarayıcı izolasyonunu bulut tabanlı bir hizmet olarak
sunar ve hizmet alan kuruluş ilişkili sunucu altyapısını yönetmek zorunda kalmadan kullanıcılarını teknolojiden 
faydalandırabilir. Kullanıcı tarama etkinliklerini ve ilgili riskleri izole etmek için sunuculara bağımlı olmayan, bunun
 yerine istemci tarafında koşan diğer bir yaklaşım yerel tarayıcı izolasyonu [2] ise tarayıcı etkinliğini kullanıcı 
 bilgisayarı üzerinden hipervizör teknoloji kullanarak sanallaştırmaya dayalıdır. İstemci tarafı çözümleri, uzaktan çö
 zümlerden farklı olarak fiziksel yalıtımı sağlamadığından güvenliği düşürür[3] ancak hizmet alan kuruluşun genel sunucu 
 maliyetlerinden kaçınmasına izin verir.
 """

print(b.split("."))
b =b.replace("\n","")
print(b.split("."))
