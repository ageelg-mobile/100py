#Ageel  9/9/2019
#100 Days of Python 
#Day 20 - Sets

fruit = {"apple","banana","cherry","Banana","apple"}

fruit.add("mango")
fruit.update({"pineapple","orange"})

for x in fruit:
    print(x)

print( "Onion is a fruit ?"  + str("onion" in fruit))