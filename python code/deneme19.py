#prime number
number=int(input("enter a number"))
prime=0
if number==1:
    print("the number you entered is not prime")
else:
    for i in range(2,number):
        if number%i==0:
            prime+=1
    if prime==0 :
        print("the number you entered is prime")
    else:
        print("the number you entered is not prime")
    
