a= "Python"
b= "Php"

ekrana_bastir = "{}----------{}".format(a,b)
ekrana_bastir1 = "{1}----------{0}".format(a,b)
ekrana_bastir2 = "{son}----------{ilk}".format(ilk=a,son=b)
ekrana_bastir3 = "{:>30}".format(a)
ekrana_bastir4 = "|{:<30}|".format(a)
ekrana_bastir5 = "|{:^30}|".format(a)


print(ekrana_bastir)
print(ekrana_bastir1)
print(ekrana_bastir2)
print(ekrana_bastir3)
print(ekrana_bastir4)
print(ekrana_bastir5)