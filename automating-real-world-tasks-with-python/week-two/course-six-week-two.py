import json, os

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

#dump() method serializes Python objects and outputs a JSON file
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# dumps() method serializes Python objects and returns a string instead of writing directly to a file
people_json = json.dumps(people, indent=2)

print(people_json)

# dump() or dumps() without indent parameter gives easier to read output
# below is the outout without indent
# [{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]