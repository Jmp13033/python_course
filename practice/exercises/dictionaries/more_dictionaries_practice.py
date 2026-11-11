"""
===========================================
Python Dictionaries - Next Steps Practice
===========================================

Use more_dictionary_notes.py if you need a hint.
Write your own answers below each challenge, then run the file.
Starter data is provided so you can focus on the new skills.
Each challenge has its own data and can be completed independently.
"""

# ==================================================
# Challenge 1 - Upgrade a Player
# ==================================================

print("\n----- Challenge 1 -----")
player = {"name": "Kai", "level": 4, "coins": 30}

# Use update() to change level to 5 and add "pet": "Dragon".
# Print the updated dictionary.
# Your code here


# ==================================================
# Challenge 2 - Backpack
# ==================================================

print("\n----- Challenge 2 -----")
hero = {"name": "Mia", "inventory": ["Map", "Potion"]}

# Add "Rope" to the inventory list using append().
# Print ONLY the first item. Expected: Map
# Then use a loop to print every inventory item on its own line.
# Your code here


# ==================================================
# Challenge 3 - Heal a Teammate
# ==================================================

print("\n----- Challenge 3 -----")
team = {
    "Kai": {"health": 100, "level": 5},
    "Mia": {"health": 60, "level": 4},
}

# Add 20 to Mia's current health in the nested dictionary.
# Print Mia's health. Expected: 80
# Print Kai's level. Expected: 5
# Your code here


# ==================================================
# Challenge 4 - Team Report
# ==================================================

print("\n----- Challenge 4 -----")
teammates = {
    "Kai": {"health": 100, "level": 5},
    "Mia": {"health": 80, "level": 4},
    "Leo": {"health": 90, "level": 3},
}

# Loop through teammates using items(). Print lines like:
# Kai - Level 5, Health 100
# Hint: each value you receive from items() is a dictionary of stats.
# Your code here


# ==================================================
# Challenge 5 - Find Affordable Games
# ==================================================

print("\n----- Challenge 5 -----")
games = [
    {"title": "Space Quest", "price": 15},
    {"title": "Dragon World", "price": 40},
    {"title": "Pixel Racer", "price": 20},
]

# You have a budget of 20.
# Loop through games and print the titles with prices of 20 or less.
# Expected titles: Space Quest and Pixel Racer
# Your code here


# ==================================================
# Challenge 6 - Total and Average
# ==================================================

print("\n----- Challenge 6 -----")
scores = {"Kai": 80, "Mia": 100, "Leo": 90}

# Use a loop to calculate the total score.
# Then calculate the average using the number of dictionary entries.
# Expected total: 270
# Expected average: 90.0
# Your code here


# ==================================================
# Challenge 7 - Count the Loot
# ==================================================

print("\n----- Challenge 7 -----")
loot = ["gem", "coin", "gem", "potion", "coin", "gem"]
counts = {}

# Count each item using a loop and get().
# Print each item and its count.
# Expected counts: gem = 3, coin = 2, potion = 1
# Hint: start a missing item's count at 0, then add 1.
# Your code here


# ==================================================
# Bonus Challenge - Add a Teammate
# ==================================================

print("\n----- Bonus Challenge -----")
party = {"Kai": {"level": 5, "health": 100}}

# Ask the user for a NEW teammate's name and level.
# Convert the level to an integer.
# Use their name as a new key in party.
# Its value should be a dictionary with their level and health of 100.
# Print every teammate's name and level.
# Your code here


# ==================================================
# Final Boss - Sell the Treasure
# ==================================================

print("\n----- Final Boss -----")
treasure = {"coin": 5, "gem": 3, "crown": 1}
prices = {"coin": 1, "gem": 10, "crown": 50}

# Each treasure key is an item; its value is the quantity you own.
# Each prices key is an item; its value is the price for ONE of it.
# Loop through treasure using items().
# Look up each item's price and multiply it by the quantity.
# Print each item's sale value, then the total value of all treasure.
# Expected sale values: coin = 5, gem = 30, crown = 50
# Expected total: 85
# Hint: use the same item key to look up its price in prices.
# Your code here
