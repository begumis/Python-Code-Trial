a=int(input("enter the hight of the tree"))
b=a
for i in range(1,a+1):
    print(b*" ",(2*i-1)*"*")
    b-=1
