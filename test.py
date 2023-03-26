# Python program to write JSON
# to a file


import json

with open("data.json", "r") as d:
	data = json.load(d)

print(data["Killers"]["21"]["Perks"][0])
print(data["Killers"]["21"]["Perk_Description"][0])
print(data["Survivors"]["1"]["Perks"])