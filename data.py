import json
import random
# Keys: Number ,Name, Perks, Perk_Description, Add_ons
with open("data.json", "r") as d:
	data = json.load(d)

# Killer_Perk = data["Players"]["Killers"]["1"]["Perks"]
# Survivor_Perks = data["Players"]["Survivors"]["1"]["Perks"]

class Killer:
	def __init__(self, Name, Perks, Perk_Description, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_description = Perk_Description
		self.Add_ons = Add_ons

	def GetKillerPerks(killer_num ,perk_num):
		print( data["Killers"][killer_num]["Perks"][perk_num])
		print(data["Killers"][killer_num]["Perk_Description"][perk_num])

	def create(self):
		pass

	# def print(self):
	# 	print(f"This is {self.Name} who has {self.Perks(data)} which means {self.Perk_description[x]}")

x = random.randint(1, 30)
y = random.randint(0,2)


Killer.GetKillerPerks(f"{x}", y)