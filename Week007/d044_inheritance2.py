#Ageel  10/05/2019
#100 Days of Python 
#Day 44 - Inheritance 2

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("My name is "+self.firstname+" "+self.lastname)
    

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("Hani","Sami",2003)
x.printname()
x.welcome()
 

