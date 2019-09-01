#Ageel  9/1/2019
#100 Days of Python 
#Day 13 - List

mywishlist = ["Raspberry Pi 3","Case","LCD","Battery"]
print("My wishlist "+str(mywishlist))
print("I can do without the "+mywishlist[3])

print("So just a reminder, my list is as follows")
mywishlist[0] = "Raspberry Pi 4"
del mywishlist[3]
for x in mywishlist:
   print(x)
