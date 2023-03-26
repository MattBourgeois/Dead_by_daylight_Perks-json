# Python program to write JSON
# to a file


import json

with open("data2.json", "r") as d:
	data = json.load(d)

print(data["Players"]["Killers"]["0"]["Name"])