#Ageel  10/19/2019
#100 Days of Python 
#Day 59 - RegEx3


import json
import re

weekTuple = ("Saturday","Sunday","Monday","Tuesday","Wendsday","Thursday","Friday")

x = json.dumps(weekTuple)

print(x)

txt = "data is the new oil"

y = re.search("data",txt)
if(y):
    print("Found data")
else:
    print("no data found")