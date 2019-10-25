#Ageel  10/25/2019
#100 Days of Python 
#Day 66 - String formating2

print("Enter the first letter of your name?")
x = input()
print("Enter the last letter of your name?")
y = input()

print("Your name starts with "+x+" and ends with "+y)


name = "Ahmed Ali"
balance = 53.44
txt = "Dear {name}, Your current balance is {balance} $"
print(txt.format(name=name,balance=balance))