#Ageel  8/23/2019
#100 Days of Python 
#Day 5 - Strings

from textwrap import wrap
x , y , z = 'apple' , 'orange' , 'limon'
basket = x + y + z
print("My basket contains "+str(wrap(basket,len(x))))
 