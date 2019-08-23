#Ageel  8/23/2019
#100 Days of Python 
#Day 5 - Strings

from textwrap import wrap
x , y , z = 'apple ' , 'orange' , 'limon '  #cheat by adding a space to unify size
basket = x + y + z 
basket = wrap(basket,len(x))                #make basket a list of items with 6 chars
print("My basket contains " + str(basket))  #print basket
 