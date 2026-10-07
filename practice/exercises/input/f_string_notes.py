# ============================================================
#                       F-STRINGS
# ============================================================
#
# F-strings are an easy way to put variables inside strings.
#
# ============================================================
# 1. WITHOUT AN F-STRING
# ============================================================

name = "Ben"

print("My name is", name)


# ============================================================
# 2. USING AN F-STRING
# ============================================================
#
# Put the letter f before the string.
#
# Then put the variable inside { }.
#
# Example:
#
# f"Hello {name}"
#

print(f"My name is {name}")


# ============================================================
# 3. MULTIPLE VARIABLES
# ============================================================

name = "Ben"
age = 12

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 4. VARIABLES CAN BE USED MULTIPLE TIMES
# ============================================================

name = "Ben"

print(f"Hello {name}!")
print(f"Nice to meet you, {name}!")
print(f"Goodbye, {name}!")


# ============================================================
# 5. F-STRINGS WITH INPUT()
# ============================================================
#
# F-strings become especially useful when combined with input().
#

name = input("What is your name? ")

print(f"Hello {name}!")


# ============================================================
# 6. USING MULTIPLE INPUTS
# ============================================================

name = input("What is your name? ")
age = input("How old are you? ")
food = input("What is your favorite food? ")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My favorite food is {food}.")


# ============================================================
# 7. PUTTING EVERYTHING INTO ONE STRING
# ============================================================

name = "Ben"
age = 12
food = "Pizza"

print(f"My name is {name}, I am {age} years old, and I like {food}.")


# ============================================================
# 8. MULTI-LINE F-STRINGS
# ============================================================
#
# Triple quotes """ allow us to create a string
# that takes up multiple lines.
#

name = "Ben"
age = 12
food = "Pizza"

print(f"""
===== MY PROFILE =====

Name: {name}
Age: {age}
Favorite food: {food}
""")


# ============================================================
# IMPORTANT
# ============================================================
#
# Remember:
#
# 1. Put f before the quotation marks.
#
# 2. Put variables inside { }.
#
# Example:
#
# name = "Ben"
# print(f"Hello {name}!")
#
# ============================================================


# ============================================================
# QUICK PRACTICE
# ============================================================
#
# What will this print?
#

name = "Alex"
age = 15

print(f"{name} is {age} years old.")


# Try changing the values of name and age.
#
# Then try adding another variable.