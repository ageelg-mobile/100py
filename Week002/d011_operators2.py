#Ageel  8/30/2019
#100 Days of Python 
#Day 11 - Operators2

arr = ["Sammy","Snow","White","Lamb","White","Snow","Sammy"]
x = arr[0]
y = arr[6]
z = x

print("Sammy equals Sammy ?"+" actually "+str(x == y))
print("Sammy same as Sammy ?"+" actually "+str(x is y))
print("Can we have Lamb ? result is "+ str("Lamb" in arr))
print("What about Bread ? result is "+ str("Bread" in arr))

print("Sammy equals Sammy ?"+" actually "+str(x == y))

print("OK , binary now")

a = 1            #000001
b = 3            #000011
c = a & b        #000001
print("Binary {} & {}".format(a,b)+ " is "+ str(c))

x = c            #000001
y = x << 3
print("Binary shift {} to the left".format(x)+ " is "+ str(y))