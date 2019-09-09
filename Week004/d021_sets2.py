#Ageel  9/9/2019
#100 Days of Python 
#Day 21 - Sets2

fruit = {"apple","banana","cherry","Banana","apple"}

fruit.add("mango")
fruit.update({"pineapple","orange"})

fruit.remove("apple")
fruit.discard("banana")  #better to use to avoid errors
fruit.pop()

print("Our basket has "+str(len(fruit))+" items")

for x in fruit:
    print(x)

print("We drop the basket")
fruit.clear() # or del to completly delete the var

print("We try to pickup some")
fruit = set({"mango","orange","peach"})

for x in fruit:
    print(x)

print( "Onion is a fruit ?"  + str("onion" in fruit))