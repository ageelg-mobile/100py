#Ageel  9/6/2019
#100 Days of Python 
#Day 18-19 - Quiz

mylist = []

mylist.append("Water")
mylist.append("Mug")
mylist.append("Coffee")

mylist.pop(0)
mylist.remove("Mug")

print(" I only have "+str(mylist))

anotherList = ["1","22","2","11"]
print("In no order "+str(anotherList))
anotherList.sort()
print("Sorted "+str(anotherList))

anotherList.reverse()
print("Reversed "+str(anotherList))



if "python" in tuple(("java","python","swift")):
    print("Found Python")
else:
    print("Didnt find Python")

