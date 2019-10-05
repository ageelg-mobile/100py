#Ageel  10/05/2019
#100 Days of Python 
#Day 45 - Iterators



class Library:
    def __init__(self,books,shelf):
            self.books = books
            self.shelf = shelf


class Science_section(Library):
     def __init__(self,books,shelf,name):
        super().__init__(books,shelf)
        self.name = name

myLib = Library(300,45)    
sySec = Science_section(100,15,"Physics books")

print("The "+sySec.name+" has "+str(sySec.books)+" books and "+str(sySec.shelf)+" shelfs")
sySec.books = 20
sySec.shelf = 4
print("Correction: The "+sySec.name+" has "+str(sySec.books)+" books and "+str(sySec.shelf)+" shelfs")