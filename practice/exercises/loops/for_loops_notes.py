"""
===========================================
🐍 Python For Loops - Lesson Notes 🐍
===========================================

A loop lets us repeat code without writing it
many times.

A for loop goes through items one at a time.
"""


# ==========================================
# Example 1 - A Simple Loop
# ==========================================

print("Example 1")

for number in range(5):
    print(number)


# What happens:
#
# number becomes:
# 0
# 1
# 2
# 3
# 4
#
# The loop runs 5 times.


# ==========================================
# Example 2 - Using range()
# ==========================================

print("\nExample 2")

for number in range(1, 6):
    print(number)


# range(1, 6) means:
#
# Start at 1
# Stop before 6
#
# Output:
# 1
# 2
# 3
# 4
# 5


# ==========================================
# Example 3 - Looping Through a List
# ==========================================

print("\nExample 3")

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


# The loop does this:
#
# First:
# fruit = "Apple"
#
# Second:
# fruit = "Banana"
#
# Third:
# fruit = "Orange"


# ==========================================
# Example 4 - Using a Loop with Text
# ==========================================

print("\nExample 4")

animals = ["Dog", "Cat", "Rabbit"]

for animal in animals:
    print("I like", animal)


# ==========================================
# Example 5 - Counting Items
# ==========================================

print("\nExample 5")

scores = [10, 20, 30, 40]

total = 0

for score in scores:
    total = total + score

print("Total score:")
print(total)


# ==========================================
# Example 6 - Using if Inside a Loop
# ==========================================

print("\nExample 6")

foods = ["Pizza", "Salad", "Burger", "Apple"]

for food in foods:

    if food == "Pizza":
        print("Pizza is my favorite!")

    else:
        print("I like", food)


# ==========================================
# Example 7 - Creating Patterns
# ==========================================

print("\nExample 7")

for i in range(5):
    print("*")


# Output:
#
# *
# *
# *
# *
# *


# ==========================================
# Example 8 - Looping Through a Game Inventory
# ==========================================

print("\nExample 8")

inventory = [
    "Sword",
    "Shield",
    "Potion",
    "Bow"
]

for item in inventory:
    print("You have:", item)


# ==========================================
# Summary
# ==========================================
#
# ✔ A loop repeats code
# ✔ for loops go through items one by one
# ✔ range() creates a sequence of numbers
# ✔ Lists and loops work great together
# ✔ You can put if statements inside loops
#
# Great job! 🎉