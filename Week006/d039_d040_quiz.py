#Ageel  10/05/2019
#100 Days of Python 
#Day 39-40 - Quiz


def powerme(number , power):    
    if power == 1:
       return number
    else:
        return number * powerme(number,(power-1))
    
print("5 to the power of 3 = "+str(powerme(5,3)))

numList = [-4,-6,-5,-1,2,3,7,9,88]

for x in numList:
   check = lambda a: a > 0
   if check(x):
       print(x)


    
