import json

with open('cases.json') as f:
  data = json.load(f)

#print(data)

# Pretty Printing JSON string back
print(json.dumps(data, indent = 4, sort_keys=True))
with open('world.json', 'w') as json_file:
  json.dump(data, json_file)