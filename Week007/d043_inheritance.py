#Ageel  10/05/2019
#100 Days of Python 
#Day 43 - Inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("My name is "+self.firstname+" "+self.lastname)


class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = Student("Hani","Sami")
x.printname()

