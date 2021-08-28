import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
z =  '{ "name":"Jaya", "age":35, "city":"Pune"}'

# parse x:
y = json.loads(x)
n= json.loads(z)

# the result is a Python dictionary:
print(y["age"])
print(y["city"])
print(n["age"])