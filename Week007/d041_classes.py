#Ageel  10/05/2019
#100 Days of Python 
#Day 41 - Classes

class fruit:
    def __init__(self,name):
        self.name = name
    def myname(self):
        print("My name is "+self.name)


f1 = fruit("Apple")
f1.myname()