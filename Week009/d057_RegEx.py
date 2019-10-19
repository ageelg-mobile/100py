#Ageel  10/19/2019
#100 Days of Python 
#Day 57 - RegEx


import re

txt = "Peter Piper picked a pack of pickeld pepers, a pack of pickeld pepers Peter piper picked"

#x = re.search("^The.*Spain$",txt)
x = re.findall("\D\sPeter",txt)

if(x):
    print("Found a match!")
    print(x)
else:    
    print("No match")