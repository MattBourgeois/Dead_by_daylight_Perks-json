import json

with open("api.json", "r") as f:
	data = json.load(f)

print(data["0"]["Name"])
