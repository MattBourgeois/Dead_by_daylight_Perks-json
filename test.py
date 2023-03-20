# Python program to write JSON
# to a file


import json

# Data to be written
dictionary = {
	"Name": "Bubba",
	"Perks": ["Knock Out", "Barbecue & Chilli", "Franklin's Demise"],
	"Perk_Description" :["Any Survivor who blinds you or stuns you using a Pallet becomes the Obsession. Anytime your Obsession switches to another Survivor by any means, that Survivor then suffers from the Oblivious Status Effect for 40/50/60 second", "After hooking a Survivor, all Survivors who are at least 60/50/40 metres away from that Hook have their Aura revealed to you for 4 seconds.", "If not recovered within 150/120/90 seconds, the lost Items will have their Charges depleted by The Entity. The Auras of lost Items are revealed to you within 32 metres and slowly fade from white to red as the timer elapses."],
	"Add_ons": ["Vegetable Oil", "Spark Plug", "Speed Limiter", "Chainsaw File", "Long Guide Bar", "Primer Bulb", "Knife Scratches", "Homemade Muffler", "Chilli", "The Grease", "The Beast's Marks", "Shop Lubricant", "Grisly Chains", "Begrimed Chains", "Rusted Chains", "Light Chassis", "Depth Gauge Rake", "Award-winning Chilli", "Iridescent Flesh", "Carburettor Tuning Guide"]
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)
