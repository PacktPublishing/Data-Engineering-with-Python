import json
with open("data.json","r") as f:
	data=json.load(f)
print(type(data))
print(data['records'][0]['name'])
