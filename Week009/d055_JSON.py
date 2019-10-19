#Ageel  10/19/2019
#100 Days of Python 
#Day 55 - JSON
import json
x = '{"name":"Camry","hp":"240","seats":"4"}'
a = {"name":"Camry","hp":"240","seats":"4"}

y = json.loads(x)
b = json.dumps(a)

print(y["name"])
print(b)