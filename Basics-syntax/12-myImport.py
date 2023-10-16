import Modules

Modules.greeting("abdighani")

getName = Modules.person1["name"]

print(getName)

print(" ")
#------------------------------------------------------------

import json

# some JSON:
personJson =  '{ "name":"AbdighaniMD", "age":24, "city":"London"}'
# parse x:
getPerson = json.loads(personJson)

# the result is a Python dictionary:
print(getPerson["city"])