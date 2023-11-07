import json
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
#convert json to python
emp=json.loads(employee)
print(emp)

#convert python object to json
emp1=json.dumps(emp)
print(emp1)

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

var = { 
	"Subjects": {
				"Maths":85,
				"Physics":90
				}
	}
with open("Sample.json", "w") as p:
	json.dump(var, p)
