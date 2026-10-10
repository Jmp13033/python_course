"""
===========================================
🐍 Python While Loops + Lists Practice 🐍
===========================================

Practice using while loops with lists!

Remember:

while condition:
    do something

Complete each challenge.
"""


# ==========================================
# Challenge 1 - Count Up
# ==========================================

# Use a while loop to print numbers 1 through 5.

print("\n----- Challenge 1 -----")

# Your code here


count = 0
while count <= 10 :
    print(count)
    count += 1
# ==========================================
# Challenge 2 - Build a List
# ==========================================

# Create an empty list called animals.
#
# Use a while loop to add 5 animals to the list.
#
# When finished, print the list.

print("\n----- Challenge 2 -----")

# Your code here
animals = []
animalCounter = 0
while animalCounter <=5 :
    animalInput = input("Name an animal")
    animals.append(animalInput)
    animalCounter += 1

print(animals)


# ==========================================
# Challenge 3 - Print a List
# ==========================================

# Create this list:
#
# fruits = ["Apple", "Banana", "Orange", "Grape"]
#
# Use a while loop to print every fruit.

print("\n----- Challenge 3 -----")

# Your code here

fruits = ["Apple", "Banana", "Orange", "Grape"]
index = 0
length = len(fruits)
while index <= length :
    print(fruits[index])
    index += 1
# ==========================================
# Challenge 4 - Shopping List
# ==========================================

# Create an empty shopping list.
#
# Use a while loop to ask the user for 3 items.
#
# Add each item to the list.
#
# Print the final shopping list.

print("\n----- Challenge 4 -----")

# Your code here


shopping = []
shoppingcounter = 0 
while shoppingcounter < 3 :
    shoppingInput = input("What should we get while shopping")
    shopping.append(shoppingInput)
    shoppingcounter += 1
print(shopping)
# =============================
# =============
# Challenge 5 - Count Down
# ==========================================

# Use a while loop to count down from 10 to 1.
#
# Then print:
#
# "Blast off!"

print("\n----- Challenge 5 -----")

# Your code here

countdown = 10 
while countdown > 0 :
    if countdown == 5 :
        print("Halfway there")
    print(countdown)
    countdown -= 1
print("Blast off")

# ==========================================
# Challenge 6 - Find an Item
# ==========================================

# Create this list:
#
# foods = ["Pizza", "Burger", "Tacos", "Pasta"]
#
# Use a while loop to look through the list.
#
# If you find "Tacos", print:
#
# "I found Tacos!"

print("\n----- Challenge 6 -----")

# Your code here

foods = ["Pizza", "Burger", "Tacos", "Pasta"]
goal = "Taco"
index = 0 
while index < len(foods) :
    if foods[index] == goal :
        print("I found the tacos")
    index += 1

# ==========================================
# ⭐ Bonus Challenge - Game Inventory
# ==========================================

# Create an empty inventory list.
#
# Keep asking the player to enter an item.
#
# Add each item to the inventory.
#
# If the player types "done", stop asking.
#
# Then print the inventory.

print("\n----- Bonus Challenge -----")

# Your code here
inventory = []
item = ""
while item != "done" :
    item = input("Enter an item")
    if item != "done" :
        inventory.append(item)
    
print(inventory)


# ==========================================
# 🏆 Final Boss - Guessing Game
# ==========================================

# Create a list of possible secret words:
#
# ["dragon", "robot", "pizza"]
#
# Ask the player to guess a word.
#
# Keep asking until they guess one
# of the secret words correctly.
#
# When they get it right, print:
#
# "You got it! 🎉"

print("\n----- Final Boss -----")

# Your code here