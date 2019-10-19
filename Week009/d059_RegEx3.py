#Ageel  10/19/2019
#100 Days of Python 
#Day 59 - RegEx3


import re

txt = "Peter Piper picked a pack of pickeld pepers, a pack of pickeld pepers Peter piper picked"

x = re.search("ter",txt)
y = re.sub("\s","_",txt)
z = re.sub("Peter","Ageel",txt,2)
print(x)
print(x.span())
print(x.string)
print(x.group())

if(x):
    print("Found a match! , first one is at ",x.start())
    print(z)
else:    
    print("No match")