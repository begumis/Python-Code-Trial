def boşluk(adet):
    for i in range(int(adet)):
        print(" ", end="")
def sag(adet):
    for i in range(int(adet)):
        print("/", end="")
def sol(adet):
    for i in range(int(adet)):
        print("\\", end="")
def atla(adet):
    for i in range(int(adet)):
        print()
def üst(cap):
    başlangıç = cap/2-1
    for i in range(int(cap/2)):
        boşluk(başlangıç-i)
        sag(1)
        boşluk(i*2)
        sol(1)
        atla(1)

def alt(cap):
    başlangıç=cap-2
    for i in range(int(cap/2)):
        boşluk(i)
        sol(1)
        boşluk(başlangıç-i*2)
        sag(1)
        atla(1)
def elmas(cap):
    üst(cap)
    alt(cap)

