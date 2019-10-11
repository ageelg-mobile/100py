#Ageel  10/11/2019
#100 Days of Python 
#Day 53-54 - quiz

import d053_d054_mymath
import datetime

a = 5
b = 7

print("Add "+str(a)+" & "+str(b)+" = "+str(d053_d054_mymath.add(a,b)))
print("Sub "+str(a)+" & "+str(b)+" = "+str(d053_d054_mymath.sub(a,b)))
print("Div "+str(a)+" & "+str(b)+" = "+str(d053_d054_mymath.divide(a,b)))
print("Mult "+str(a)+" & "+str(b)+" = "+str(d053_d054_mymath.multiply(a,b)))

print("The Year is "+str(datetime.datetime.now().year))
print("The Day Date and Time "+str(datetime.datetime.now().strftime("%c")))
print("The Day is "+str(datetime.datetime.now().strftime("%A")))
print("The Month is "+str(datetime.datetime.now().strftime("%B")))


yesterday = datetime.datetime.now()
yesterday -= datetime.timedelta(days=1)
tomorrow = datetime.datetime.now()
tomorrow += datetime.timedelta(days=1)
print("The Day Date and Time "+str(yesterday.strftime("%c")))
print("The Day Date and Time "+str(tomorrow.strftime("%c")))
