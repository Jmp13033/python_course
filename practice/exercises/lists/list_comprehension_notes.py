"""
===========================================
🐍 Python List Comprehensions - Notes 🐍
===========================================

A list comprehension is a short way to create
a new list from another list.

The basic pattern is:

[WHAT_TO_ADD for ITEM in LIST]
"""


# ==========================================
# Example 1 - Regular For Loop
# ==========================================

print("Example 1 - Regular For Loop")

numbers = [1, 2, 3, 4, 5]

doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)


# ==========================================
# Example 2 - List Comprehension
# ==========================================

print("\nExample 2 - List Comprehension")

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)


"""
These two programs do the SAME thing:

Regular loop:

doubled = []

for number in numbers:
    doubled.append(number * 2)


List comprehension:

doubled = [number * 2 for number in numbers]

The list comprehension is simply shorter!
"""


# ==========================================
# Example 3 - Basic List Comprehension
# ==========================================

print("\nExample 3")

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# ==========================================
# Example 4 - Using Strings
# ==========================================

print("\nExample 4")

names = ["alex", "sarah", "mike", "jordan"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)


# ==========================================
# Example 5 - Adding a Number
# ==========================================

print("\nExample 5")

numbers = [5, 10, 15, 20]

new_numbers = [number + 10 for number in numbers]

print(new_numbers)


# ==========================================
# Example 6 - Using an Expression
# ==========================================

print("\nExample 6")

numbers = [1, 2, 3, 4, 5]

tripled = [number * 3 for number in numbers]

print(tripled)


# ==========================================
# Example 7 - Filtering with if
# ==========================================

print("\nExample 7")

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


"""
This means:

Take each number from numbers
BUT only add it if:

number % 2 == 0

So we get:

[2, 4, 6]
"""


# ==========================================
# Example 8 - Filtering Big Numbers
# ==========================================

print("\nExample 8")

numbers = [5, 20, 8, 100, 3, 50]

big_numbers = [
    number
    for number in numbers
    if number > 10
]

print(big_numbers)


# ==========================================
# Example 9 - Strings with if
# ==========================================

print("\nExample 9")

foods = ["Pizza", "Salad", "Burger", "Pasta"]

long_food_names = [
    food
    for food in foods
    if len(food) > 5
]

print(long_food_names)


# ==========================================
# Example 10 - Game Scores
# ==========================================

print("\nExample 10")

scores = [10, 25, 50, 100]

double_scores = [score * 2 for score in scores]

print("Original scores:")
print(scores)

print("Double scores:")
print(double_scores)


# ==========================================
# Example 11 - Game Inventory
# ==========================================

print("\nExample 11")

inventory = ["sword", "shield", "potion", "bow"]

inventory_upper = [
    item.upper()
    for item in inventory
]

print(inventory_upper)


# ==========================================
# Breaking Down the Syntax
# ==========================================

"""
Look at this:

doubled = [number * 2 for number in numbers]

There are three important parts:

1. WHAT DO WE WANT TO ADD?

   number * 2


2. WHAT VARIABLE ARE WE USING?

   number


3. WHERE ARE WE GETTING THE ITEMS?

   numbers


So:

[number * 2 for number in numbers]

means:

"Take every number from numbers,
multiply it by 2,
and put the result into a new list."
"""


# ==========================================
# Regular Loop vs Comprehension
# ==========================================

print("\nRegular Loop vs List Comprehension")

numbers = [1, 2, 3, 4, 5]

# Regular loop

squares = []

for number in numbers:
    squares.append(number * number)

print("Regular loop:")
print(squares)


# List comprehension

squares = [number * number for number in numbers]

print("List comprehension:")
print(squares)


# ==========================================
# ⚠️ Important
# ==========================================

"""
List comprehensions are great when the operation
is simple and easy to understand.

Don't try to make everything a list comprehension.

For example, this is easy to understand:

squares = [number * number for number in numbers]


But if a comprehension becomes extremely long
or complicated, a regular for loop may be better.

Readable code is important!
"""


# ==========================================
# Summary
# ==========================================

"""
✔ List comprehensions create NEW lists

✔ They are a shorter way to write certain
  for loops

✔ They can transform items

✔ They can filter items using if

✔ They work especially well with lists

Basic pattern:

[WHAT_TO_ADD for ITEM in LIST]

With a condition:

[WHAT_TO_ADD for ITEM in LIST if CONDITION]

Great job! 🎉
"""