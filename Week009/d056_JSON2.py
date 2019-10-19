#Ageel  10/19/2019
#100 Days of Python 
#Day 56 - JSON2

import json
a = {"name":"Camry","hp":"240","seats":"4"}

b = json.dumps(a,indent=2,separators=(", "," : "),sort_keys=True)

print(b)
