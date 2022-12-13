"""
https://www.programiz.com/python-programming/json

"""



"""
Example 1: Python JSON to dict
You can parse a JSON string using json.loads() method. The method returns a dictionary.
"""
import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']


print(person_dict['languages'])

"""
Example 2: Python read JSON file
You can use json.load() method to read a file containing JSON object.

Suppose, you have a file named person.json which contains a JSON object.
"""

{"name": "Bob",
"languages": ["English", "Fench"]
}
"""
Here's how you can parse this file:

 """
import json

with open('path_to_file/person.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)

"""
Here, we have used the open() function to read the json file. Then, the file is parsed using json.load() method which gives us a dictionary named data.

"""


"""
Python Convert to JSON string
You can convert a dictionary to JSON string using json.dumps() method.

Example 3: Convert dict to JSON"""

import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
