"""
===========================================
🐍 Python For Loops Practice 🐍
===========================================

Practice using for loops!

Remember:

for item in list:
    do something

Complete each challenge.
"""


# ==========================================
# Challenge 1 - Loop Through a List
# ==========================================

# Create a list of 5 animals.
#
# Use a for loop to print each animal.

print("\n----- Challenge 1 -----")

# Your code here
animals = ["Dog", "Cat", "Lion", "Tiger", "Elephant"]
for animal in animals:
    print(animal)



# ==========================================
# Challenge 2 - Say Hello
# ==========================================

# Create a list of 5 names.
#
# Use a loop to print:
#
# Hello Alex
# Hello Sarah
#
# (Your names will be different.)

print("\n----- Challenge 2 -----")

# Your code here
names = ["Carter", "James", "Mia", "Ben", "Anthony"]
for name in names:
    print("Hello", name)



# ==========================================
# Challenge 3 - Game Inventory
# ==========================================

# Create an inventory list:
#
# Sword
# Shield
# Potion
# Bow
#
# Use a loop to print:
#
# You have Sword
# You have Shield

print("\n----- Challenge 3 -----")

# Your code here
inventory = ["Sword", "Sheild", "Potion", "Bow"]
for item in inventory:
    print("You have a ", item )



# ==========================================
# Challenge 4 - Count Numbers
# ==========================================

# Create a list of numbers:
#
# [5, 10, 15, 20]
#
# Use a loop to add all the numbers together.
#
# Expected output:
# 50

print("\n----- Challenge 4 -----")

# Your code here
numbers = [5, 10, 15, 20]
for number in numbers:
    print(number)


# ==========================================
# Challenge 5 - Find a Favorite Food
# ==========================================

# Create a list of foods.
#
# Use a loop:
#
# If the food is "Pizza":
# print "I found my favorite food!"
#
# Otherwise:
# print "I like <food>"

print("\n----- Challenge 5 -----")

# Your code here
fav_food = ["Soup", "Waffles", "Pizza"]
for food in fav_food:
    if food == "Pizza":
        print("I found my favorite food!")
    else:
        print(f"I like {food}")



# ==========================================
# Challenge 6 - range()
# ==========================================

# Use range() to print numbers from 1 to 10.

print("\n----- Challenge 6 -----")

# Your code here
range(10)
for number in range(1, 11, 3):
    print(number)



# ==========================================
# Challenge 7 - Multiplication Table
# ==========================================

# Use a loop to print the 5 times table.
#
# Example:
#
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15

print("\n----- Challenge 7 -----")

# Your code here
range(10)
for number in range(15):
    print(f"{number} * 5 {5 * number}")

for i in range(1, 13):
    print(f"5 x {i} = {5 * i}")



# ==========================================
# ⭐ Bonus Challenge - Player Scores
# ==========================================

# A game has these scores:
#
# scores = [100, 250, 300, 150]
#
# Use a loop to find the total score.
#
# Expected output:
# 800

print("\n----- Bonus Challenge -----")

# Your code here



# ==========================================
# 🏆 Final Boss Challenge
# ==========================================

# Create a list of 5 monsters:
#
# "Dragon"
# "Goblin"
# "Troll"
# "Zombie"
# "Skeleton"
#
# Use a loop to print:
#
# Fighting Dragon!
# Fighting Goblin!
#
# Bonus:
# Ask the user for a monster name
# and add it to the list.

print("\n----- Final Boss -----")

# Your code here