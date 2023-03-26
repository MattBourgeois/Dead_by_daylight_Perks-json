import json
import random
# Keys: Number ,Name, Perks, Perk_Description, Add ons

with open("data.json", "r") as d:
	data = json.load(d)

# print(data["Players"]["Killers"]['5']["Perks"])
# print(data["Players"]["Killers"]['5']['Perks'][0])  #Gets the Perk
# print(data["Players"]["Killers"]["5"]["Perk_Description"][0]) #Gets the perk Description


# print(data["Players"]["Killers"]["0"]["Name"])
# print(data["Players"]["Survivors"]["0"]["Name"])
# for x in range(0, len(data)):
# 	print(data["Players"]["Killers"]["0"]["Name"])



# Creates new json file 
with open("data2.json", "w") as f: 
	json.dump(data, f)