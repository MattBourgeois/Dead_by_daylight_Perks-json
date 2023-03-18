import json
# Keys: Perks, 
with open("api.json", "r") as f:
	data = json.load(f)

print(data["20"]["Perks"][0])
print(data["20"]["Perk Descriptions"][0])
