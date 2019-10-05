#Ageel  10/05/2019
#100 Days of Python 
#Day 34 - Functions 2

def addOneTill10(x,y): 
  y -= 1
  x += 1
  print(x)

  if(x==10): 
    return x
  else:
     addOneTill10(x,y)
   


addOneTill10(x=6,y=50)
       




