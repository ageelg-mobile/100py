#Ageel  10/19/2019
#100 Days of Python 
#Day 58 - RegEx


import re

txt = "Peter Piper picked a pack of pickeld pepers, a pack of pickeld pepers Peter piper picked"

x = re.search("ter",txt)
y = re.split("\s",txt)
print(x)

if(x):
    print("Found a match! , first one is at ",x.start())
    print(y)
else:    
    print("No match")