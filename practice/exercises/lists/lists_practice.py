"""
===========================================
🐍 Python Lists Practice Challenge 🐍
===========================================

Instructions:
Complete each challenge by writing your own code.
Run the program after each challenge to make sure it works!

Good luck!
"""

# ==================================================
# Challenge 1 - Create a List
# ==================================================

# Create a list called "colors"
# Add your three favorite colors to the list.
#
# Example:
# colors = ["Blue", "Green", "Red"]


print("\n----- Challenge 1 -----")
# Print your list here.

colors = ["Orange" "Red" "Blue"]
print(colors)
# ==================================================
# Challenge 2 - Indexing
# ==================================================

# Print ONLY the first color.
#
# Expected Output (example):
# Blue

print("\n----- Challenge 2 -----")

print(colors(0))
# ==================================================
# Challenge 3 - Change an Item
# ==================================================

# Change the SECOND color to "Purple".
#
# Print the whole list afterward.
#
# Expected Output (example):
# ['Blue', 'Purple', 'Red']

print("\n----- Challenge 3 -----")

colors[1] = "Purplr"
print (colors)
# ==================================================
# Challenge 4 - Add an Item
# ==================================================

# Add "Gold" to the END of the list using append().
#
# Print the updated list.

print("\n----- Challenge 4 -----")

colors.append("Gold")
print(colors)
# ==================================================
# Challenge 5 - Remove an Item
# ==================================================

# Remove "Gold" from the list.
#
# Print the updated list.

print("\n----- Challenge 5 -----")

colors.remove("Gold")
print(colors)
# ==================================================
# Challenge 6 - Length
# ==================================================

# Print how many colors are in your list.
#
# Example Output:
# 3

print("\n----- Challenge 6 -----")
print(len(colors))

# ==================================================
# Challenge 7 - Loop Through a List
# ==================================================

# Print every color using a for loop.
#
# Example Output:
# Blue
# Purple
# Red

print("\n----- Challenge 7 -----")

for color in colors :
    print(color)

# ==================================================
# Challenge 8 - Favorite Foods
# ==================================================

# Create a list called foods.
#
# Add FOUR of your favorite foods.

print("\n----- Challenge 8 -----")

Foods = ["Chicken" "Steak" "Tuna" "Cheese"]
# ==================================================
# Challenge 9 - Print Each Food
# ==================================================

# Use a for loop to print:
#
# I like Pizza
# I like Tacos
# I like Pasta
#
# (Your foods will be different.)

print("\n----- Challenge 9 -----")

for Food in Foods :
    print("I like " + Food)

# ==================================================
# Challenge 10 - User Input
# ==================================================

# Create an empty list called animals.
#
# Ask the user:
# "What is your favorite animal?"
#
# Add their answer to the list.
#
# Print the whole list.

print("\n----- Challenge 10 -----")

Animals = []
Animal = input("What is your favorite animal?")
Animals.append(Animal)
print(Animals)
# ==================================================
# ⭐ Bonus Challenge 1
# ==================================================

# Create a list of FIVE video games.
#
# Print ONLY the last game.

print("\n----- Bonus 1 -----")


# ==================================================
# ⭐ Bonus Challenge 2
# ==================================================

# Create a list of FIVE superheroes.
#
# Replace one superhero with another.
#
# Print the updated list.

print("\n----- Bonus 2 -----")


# ==================================================
# ⭐ Bonus Challenge 3
# ==================================================

# Create a list of FIVE numbers.
#
# Print the sum of the FIRST TWO numbers.
#
# Example:
# numbers = [10, 20, 30, 40, 50]
#
# Output:
# 30

print("\n----- Bonus 3 -----")


# ==================================================
# ⭐ Bonus Challenge 4
# ==================================================

# Print every color from your colors list again,
# but this time make each line say:
#
# My favorite color is Blue
# My favorite color is Purple
# My favorite color is Red

print("\n----- Bonus 4 -----")


# ==================================================
# 🏆 Final Boss Challenge
# ==================================================

# Create an empty shopping list.
#
# Ask the user to enter THREE grocery items.
#
# Add each item to the list.
#
# When finished, print:
#
# My Shopping List
# ----------------
# - Apples
# - Milk
# - Bread
#
# (Your items will be different.)

print("\n----- Final Boss -----")