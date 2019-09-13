#Ageel  9/13/2019
#100 Days of Python 
#Day 22 - Disctionary 2

employees = {"2001":"Ahmed","2002":"Salem","2003":"Waseem"}

print("we have a total of "+str(len(employees))+ " employees")

employees["2004"] = "Jafar"
employees.pop("2001")
employees.popitem()
del employees["2002"]

if "Jafar" in employees.values():
        print("Jafar is an employee in our company")
else:
        print("Jafar is not an employee in our company")


employees.clear()
del employees

