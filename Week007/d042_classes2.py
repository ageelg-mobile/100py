#Ageel  10/05/2019
#100 Days of Python 
#Day 42 - Classes 2

class fruit:
    def __init__(self,name):
        self.name = name
    def myname(self):
        print("My name is "+self.name)


f1 = fruit("Apple")
f1.name = "Orange"
#del f1.name 
#del f1
f1.myname()