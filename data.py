import json
# Keys: Number ,Name, Perks, Perk_Description, Add_ons
with open("data.json", "r") as d:
	data = json.load(d)

Killer_Perk = data["Players"]["Killers"]["1"]["Perks"]
Survivor_Perks = data["Players"]["Survivors"]["1"]["Perks"]

class Killer:
	def __init__(self, Name, Perks, Perk_description, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_description = Perk_description
		self.Add_ons = Add_ons

	def GetKillerPerks(self, Name, Perks, Perk_Description, Add_ons):
		return data["Player"]["Killer"]["Perks"]

	def create(self):
		
		pass

	# def print(self):
	# 	print(f"This is {self.Name} who has {self.Perks(data)} which means {self.Perk_description[x]}")

# Killer.GetKillerPerks(self, Name, Perks, Perk_Description, Add_ons)

print(Killer_Perk)