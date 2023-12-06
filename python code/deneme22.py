def factorial(number):
    result=1
    if number==1 or number==0:
        print("factorial=1")
    elif number > 1:
        for i in range(1,number+1):
            result*=i
        print("factorial=",result)
    else :
       print("please enter a new number bigger than 0")
       
number=int(input("please enter a number")) 
factorial(number)
            
                            
