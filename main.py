import json
# Keys: Perks, 
with open("api.json", "r") as f:
	data = json.load(f)

for i in data:
	print(data['Name'])

# print(data["Name"]["Perks"])
# print(data["20"]["Perk Descriptions"][0])
