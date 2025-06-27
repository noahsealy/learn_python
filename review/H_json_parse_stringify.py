# this program will parse the json, then stringify it again

# The term “object” in the context of JSON processing in Python can be ambiguous.
#  All values in Python are objects. In JSON, an object refers to any data wrapped in curly braces, 
# similar to a Python dictionary.

import json

def add_employee(salaries_json, name, salary):
    # convert the string to the object datastructure
    # json.loads() method of JSON module is used to parse a valid JSON string and convert it into a Python dictionary.
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    # return it back as a string
    # json.dumps() function will convert a subset of Python objects into a json string
    return json.dumps(salaries)

salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])