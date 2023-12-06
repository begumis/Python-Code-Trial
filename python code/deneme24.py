"""def calculate(vize,final,vizepercentage,finalpercentage):
    return vize*vizepercentage/100+final*finalpercentage/100

print(calculate(50,70,30,70))"""
          
def numbers(number):
    sum=0
    for i in range(len(number)):
        if number[i]%2!=0:
            sum+=number[i]
    return sum
print(numbers([2,3,4,5,6,7,8]))

    
