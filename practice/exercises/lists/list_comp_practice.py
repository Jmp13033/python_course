"""
===========================================
🐍 Python List Comprehensions Practice 🐍
===========================================

A list comprehension lets us create a new list
using a single line of code.

Example:

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

Output:
[2, 4, 6, 8, 10]


Remember:

[WHAT_TO_ADD for ITEM in LIST]
"""


# ==========================================
# Challenge 1 - Double the Numbers
# ==========================================

# Create a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Use a list comprehension to create a new list
# containing each number multiplied by 2.
#
# Expected output:
# [2, 4, 6, 8, 10]

print("\n----- Challenge 1 -----")

# Your code here

numbers = [1,2,3,4,5]
doubled = [number * 2 for number in numbers]
numbers_list = [1,2,3,4,5]
doubled_list = []
for number in numbers_list:
    doublednumber =2 * number
    doubled_list.append(doublednumber)
print(doubled_list)
# ==========================================
# Challenge 2 - Square the Numbers
# ==========================================

# Create a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Create a new list containing each number
# squared.
#
# Expected output:
# [1, 4, 9, 16, 25]

print("\n----- Challenge 2 -----")

# Your code here

numbers = [1,2,3,4,5]
squares = [numbers * numbers for number in numbers]

# ==========================================
# Challenge 3 - Make Everything Bigger
# ==========================================

# Create a list of names:
#
# names = ["alex", "sarah", "mike", "jordan"]
#
# Use a list comprehension to create a new list
# where every name is uppercase.
#
# Hint:
# .upper()
#
# Expected output:
# ["ALEX", "SARAH", "MIKE", "JORDAN"]

print("\n----- Challenge 3 -----")

# Your code here
names = ["alex", "sarah", "mike", "jordan"]
upper_names = [names.upper() for name in names]
print(upper_names)


# ==========================================
# Challenge 4 - Add 10
# ==========================================

# Create:
#
# numbers = [5, 10, 15, 20]
#
# Use a list comprehension to add 10
# to every number.
#
# Expected output:
# [15, 20, 25, 30]

print("\n----- Challenge 4 -----")

# Your code here

numbers = [5,10,15,20]
added_numbers = [numbers + 10 for number in numbers]
print(added_numbers)

# ==========================================
# Challenge 5 - Get Even Numbers
# ==========================================

# Create:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# Use a list comprehension to create a new list
# containing ONLY the even numbers.
#
# Expected output:
# [2, 4, 6, 8]

print("\n----- Challenge 5 -----")

# Your code here

numbers = [1,2,3,4,5,6,7,8]
even_numbers = [numbers for number in numbers if number % 2 == 0]
print(even_numbers)
odd_numbers = [numbers for number in numbers if number % 2 != 0]
print(odd_numbers)
# ==========================================
# Challenge 6 - Get Big Numbers
# ==========================================

# Create:
#
# numbers = [5, 20, 8, 100, 3, 50]
#
# Create a new list containing only numbers
# greater than 10.
#
# Expected output:
# [20, 100, 50]

print("\n----- Challenge 6 -----")

# Your code here

numbers = [5, 20, 8, 100, 3, 50]
big_numbers = [number for number in numbers if number > 10]

# ==========================================
# ⭐ Bonus Challenge - Game Scores
# ==========================================

# Create:
#
# scores = [10, 25, 50, 100]
#
# Create a new list where every score
# is doubled.
#
# Expected output:
# [20, 50, 100, 200]

print("\n----- Bonus Challenge -----")

# Your code here

scores = [10, 25, 50, 100]
doubled_scores = [scores * 2 for score in scores]

# ==========================================
# 🏆 Final Boss - Shopping List
# ==========================================

# Create:
#
# shopping = ["apple", "milk", "bread", "eggs"]
#
# Use a list comprehension to create a new list
# where every item is uppercase.
#
# Expected output:
#
# ["APPLE", "MILK", "BREAD", "EGGS"]
#
# BONUS:
# Try creating the same result using
# a regular for loop first.
#
# Then create it using a list comprehension.
#
# Which one is shorter?

print("\n----- Final Boss -----")

# Your code here

shopping = ["apple", "milk", "bread", "eggs"]
Upper_shopping = [item.upper() for item in shopping]
shopping_upper = ["apple", "milk", "bread", "eggs"]
shop_upper = []
for item in shopping_upper:
    shop_upper.append(item.upper())