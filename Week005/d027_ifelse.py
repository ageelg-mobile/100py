#Ageel  9/25/2019
#100 Days of Python 
#Day 27 - If Else

a = 60
b = 40
c = 40
e = 50

if a > b:
     print("a is bigger than b") 
elif a < b: 
    print("a is smaller than b ")
else:
    print("a is equal to b")

print("c > b") if c > b else print(" c < b ") if c < b else  print("c = b")

if a > b and a > c and a > e : print("A is the biggest") 