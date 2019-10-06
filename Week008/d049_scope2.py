#Ageel  10/06/2019
#100 Days of Python 
#Day 49 - Scope



def myfun():
 y = 700
 def myfun2():
  global x
  x = 300
  print(y)
 myfun2()
myfun()
print(x)