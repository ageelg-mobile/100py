#Ageel  10/25/2019
#100 Days of Python 
#Day 64 - Try Except

print("Enter your age")
x = input()
try: 
    y = int(x)
    print("You are "+str(y)+" old")
except ValueError:
    print("Please enter a number")
except:
    print("Opps , didnt work")
else:
    print("have a nice day")    
finally:
    print("Thanks")    