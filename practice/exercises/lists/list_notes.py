"""
===========================================
🐍 Python Lists - Lesson Notes 🐍
===========================================

A list lets you store multiple values in one variable.

Example:
"""

# Creating a list
fruits = ["Apple", "Banana", "Orange"]

print(fruits)

# --------------------------------------------------

"""
Getting items from a list

Lists start counting at ZERO.

Index:
0        1         2
Apple   Banana   Orange
"""

print("\nFirst fruit:")
print(fruits[0])

print("\nSecond fruit:")
print(fruits[1])

print("\nThird fruit:")
print(fruits[2])

# --------------------------------------------------

"""
Changing an item in a list
"""

fruits[1] = "Watermelon"

print("\nAfter changing Banana to Watermelon:")
print(fruits)

# --------------------------------------------------

"""
Adding an item

append() adds an item to the END of the list.
"""

fruits.append("Grapes")

print("\nAfter adding Grapes:")
print(fruits)

# --------------------------------------------------

"""
Removing an item

remove() removes the item you specify.
"""

fruits.remove("Apple")

print("\nAfter removing Apple:")
print(fruits)

# --------------------------------------------------

"""
Finding the length of a list

len() tells you how many items are in a list.
"""

print("\nNumber of fruits:")
print(len(fruits))

# --------------------------------------------------

"""
Lists can store numbers too.
"""

scores = [95, 87, 100, 76]

print("\nScores:")
print(scores)

print("First score:")
print(scores[0])

# --------------------------------------------------

"""
Lists can store almost anything!
"""

animals = ["Dog", "Cat", "Rabbit"]
numbers = [10, 20, 30]
mixed = ["Alex", 12, True]

print("\nAnimals:")
print(animals)

print("\nNumbers:")
print(numbers)

print("\nMixed List:")
print(mixed)

# --------------------------------------------------

"""
Summary

✔ Create a list
✔ Get an item using []
✔ Change an item
✔ Add an item with append()
✔ Remove an item with remove()
✔ Count items with len()

Great job! 🎉
"""