#Ageel  9/6/2019
#100 Days of Python 
#Day 17 - Tuples 2

fruit = ("apple","banana","cherry")

if "onion" in fruit:
    print("onion is a fruit !")
else:
    print("onion is NOT a  fruit !")


fruit2 = ("apple",) * 12
print("We have a dozen apples")
print(fruit2)

fruit3 = tuple(("orange","orange")) 
print("and two oranges")
print(fruit3)


fruit4 = fruit + fruit2 + fruit3
print("In total , we hvae "+str(len(fruit4))+ " fruits")
print(fruit4)