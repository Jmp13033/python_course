"""
===========================================
Python Dictionaries Practice
===========================================

Complete each challenge by writing your own code below it.
Run the file after each challenge to check your work.
Use dictionary_notes.py if you need a reminder!

Challenges 1-9 use the same player dictionary.
Leave your earlier answers in place as you continue.
"""

# ==================================================
# Challenge 1 - Create a Player
# ==================================================

# Create a dictionary called player with these pairs:
# "name": a player name of your choice
# "level": 1
# "health": 100
# Print the whole dictionary.

print("\n----- Challenge 1 -----")
# Your code here


# ==================================================
# Challenge 2 - Read Values
# ==================================================

# Print ONLY the player's name.
# Then print ONLY the player's health.
# Use the keys to look up the values.

print("\n----- Challenge 2 -----")
# Your code here


# ==================================================
# Challenge 3 - Level Up
# ==================================================

# Change the player's level to 2.
# Print a message using an f-string, like:
# You are now level 2!

print("\n----- Challenge 3 -----")
# Your code here


# ==================================================
# Challenge 4 - Take Damage
# ==================================================

# Subtract 25 from the player's CURRENT health.
# Store the result back in the dictionary.
# Print the remaining health. Expected: 75

print("\n----- Challenge 4 -----")
# Your code here


# ==================================================
# Challenge 5 - Find Treasure
# ==================================================

# Add a new key called "coins" with a value of 50.
# Add another key called "weapon" with a value of "Bow".
# Print the dictionary.

print("\n----- Challenge 5 -----")
# Your code here


# ==================================================
# Challenge 6 - Remove a Weapon
# ==================================================

# Use pop() to remove "weapon" and store its value in a variable.
# Print the removed weapon, then print the dictionary.

print("\n----- Challenge 6 -----")
# Your code here


# ==================================================
# Challenge 7 - Check for a Pet
# ==================================================

# Use get() to print the value of "pet".
# If that key is missing, display "No pet yet".
# Expected: No pet yet

print("\n----- Challenge 7 -----")
# Your code here


# ==================================================
# Challenge 8 - Count and Check
# ==================================================

# Print the number of pairs in player. Expected: 4
# Use an if statement to check whether "coins" is a key.
# If it is, print "You found treasure!"

print("\n----- Challenge 8 -----")
# Your code here


# ==================================================
# Challenge 9 - Show the Profile
# ==================================================

# Use a for loop and items() to print each key and value.
# Example (your name may be different):
# name: Alex
# level: 2
# health: 75
# coins: 50

print("\n----- Challenge 9 -----")
# Your code here


# ==================================================
# Challenge 10 - Build Your Own Profile
# ==================================================

# Create an EMPTY dictionary called profile.
# Ask the user for their name, age, and favorite game.
# Store each answer under a descriptive key in profile.
# Convert the age to an integer.
# Print the completed dictionary.

print("\n----- Challenge 10 -----")
# Your code here


# ==================================================
# Bonus Challenge - Inventory
# ==================================================

# Create an inventory dictionary with:
# "potions": 3, "arrows": 10, "gems": 2
# Use a potion by subtracting 1 from its current quantity.
# Loop through the dictionary to print each item and quantity.
# Add up all quantities and print the total. Expected: 14

print("\n----- Bonus Challenge -----")
# Your code here


# ==================================================
# Final Boss - Game Shop
# ==================================================

# Create a shop dictionary with these item prices:
# "sword": 40, "shield": 30, "potion": 10
# Start with 50 coins in a variable called coins.
# Print each item and price using a loop.
# Ask the user which item they want to buy.
# If the item exists in the shop:
#   If they have enough coins, subtract the price and print
#   the item they bought and their remaining coins.
#   Otherwise, print "Not enough coins!"
# If the item does not exist, print "That item is not in the shop."
# Try buying "shield" (20 coins left) and an item not in the shop.

print("\n----- Final Boss -----")
# Your code here
