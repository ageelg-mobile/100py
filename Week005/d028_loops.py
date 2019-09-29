#Ageel  9/29/2019
#100 Days of Python 
#Day 28 - Loops

i = 10

while i > 0:
    
    if (i == 7): #skip 7
     i -= 1
     continue
    print(str(i))
    i -= 1
else: 
    print("I is less than 0")