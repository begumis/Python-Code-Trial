def faktöriyel(sayı):
    sonuc = 1
    for a in range(sayı):
        b=a+1
        sonuc *=b
    return sonuc

print(faktöriyel(6))

def faktöriyel2(sayı):
    if sayı == 1:
         return 1
    else:
        return sayı * faktöriyel2(sayı-1)

print(faktöriyel2(6))