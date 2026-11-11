"""
===========================================
Python Dictionaries - Lesson Notes
===========================================

A dictionary stores pairs of KEYS and VALUES.
Think of a key as a label and its value as the information.
Lists use numbered positions. Dictionaries use keys.

Run this file to see each example!
"""

# ==================================================
# 1 - Create a Dictionary
# ==================================================

# Use curly braces {}, colons between keys and values,
# and commas between pairs. String keys need quotes.
player = {
    "name": "Alex",
    "level": 5,
    "health": 100,
}

print("Player:")
print(player)

# Each key is unique. Values can be strings, numbers, lists, and more.
# Writing the same key again replaces its old value.

# ==================================================
# 2 - Get a Value
# ==================================================

# Put the KEY inside square brackets, not a numbered position.
print("\nPlayer name:")
print(player["name"])

# Keys are case-sensitive: "name" and "Name" are different keys.
# Square brackets cause a KeyError if the key does not exist.
# get() can return a default value instead.
print(player.get("pet", "No pet yet"))

# ==================================================
# 3 - Change a Value
# ==================================================

player["level"] = 6
player["health"] = player["health"] - 20
print("\nAfter leveling up and taking damage:")
print(player)

# ==================================================
# 4 - Add a New Pair
# ==================================================

# Assigning to a NEW key adds that key and value.
player["weapon"] = "Sword"
print("\nAfter adding a weapon:")
print(player)

# ==================================================
# 5 - Remove a Pair
# ==================================================

# pop() removes a key AND returns its value.
weapon = player.pop("weapon")
print("\nRemoved weapon:", weapon)
print(player)

# ==================================================
# 6 - Count and Check Keys
# ==================================================

print("\nNumber of pairs:", len(player))

# 'in' checks the KEYS, not the values.
if "health" in player:
    print("The player has a health value!")

# ==================================================
# 7 - Loop Through a Dictionary
# ==================================================

print("\nKeys:")
for key in player:
    print(key)

print("\nValues:")
for value in player.values():
    print(value)

# items() gives you each key and its value together.
print("\nPlayer profile:")
for key, value in player.items():
    print(f"{key}: {value}")

# ==================================================
# 8 - Start Empty and Add Input
# ==================================================

# Example (remove the # from these lines to try it):
# profile = {}
# profile["name"] = input("What is your name? ")
# profile["age"] = int(input("How old are you? "))
# print(profile)

"""
Quick reference:
Create:       player = {"name": "Alex"}
Read:         player["name"]
Read safely:  player.get("pet", "No pet yet")
Change/add:   player["level"] = 6
Remove:       player.pop("level")
Count pairs:  len(player)
Check a key:  "name" in player
Loop pairs:   for key, value in player.items():

Next: try dictionaries_practice.py!
"""
