def ucgen(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(ucgen(3,4,5))

ucgen2 = lambda a,b,c: a**2 + b**2 == c**2

print(ucgen2(3,4,6))