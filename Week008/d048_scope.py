#Ageel  10/06/2019
#100 Days of Python 
#Day 48 - Scope

x = 300

def myfun():
 y = 700
 print(x)  
 def myfun2():
  print(y)
 myfun2()
myfun()