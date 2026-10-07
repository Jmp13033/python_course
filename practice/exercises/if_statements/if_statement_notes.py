# ============================================================
#                     IF STATEMENTS
# ============================================================
#
# An if statement allows our program to make decisions.
#
# It basically means:
#
# "IF something is true, do this."
#
# ============================================================


# ============================================================
# 1. A SIMPLE IF STATEMENT
# ============================================================

age = 18

if age >= 18:
    print("You are an adult.")


# ============================================================
# IMPORTANT
# ============================================================
#
# Notice the colon : after the condition.
#
# Also notice that the print() is indented.
#
# This indentation tells Python:
#
# "This code belongs to the if statement."
#
# Example:
#
# if age >= 18:
#     print("You are an adult.")
#
# ============================================================


# ============================================================
# 2. IF WITH A NUMBER
# ============================================================

score = 100

if score == 100:
    print("Perfect score!")


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================
#
# Python has several operators we can use to compare values.
#
# ==    Equal to
# !=    Not equal to
# >     Greater than
# <     Less than
# >=    Greater than or equal to
# <=    Less than or equal to
#
# ============================================================


age = 15

if age > 10:
    print("You are older than 10.")


# ============================================================
# 4. EQUAL TO ==
# ============================================================
#
# Be careful!
#
# =  means "assign a value"
#
# == means "compare two values"
#
# Example:
#

name = "Ben"

if name == "Ben":
    print("Hello Ben!")


# ============================================================
# 5. IF AND INPUT()
# ============================================================
#
# We can use input() to let the user make a decision.
#

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")


# ============================================================
# 6. IF AND F-STRINGS
# ============================================================

name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18:
    print(f"Hello {name}, you are an adult.")


# ============================================================
# 7. ELSE
# ============================================================
#
# Sometimes we want to do one thing if something is true,
# and something different if it is false.
#
# That's what else is for.
#

age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")


# ============================================================
# 8. IF / ELSE WITH INPUT
# ============================================================

age = int(input("How old are you? "))

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# ============================================================
# 9. ELIF
# ============================================================
#
# elif means:
#
# "If the previous condition wasn't true,
#  check this condition."
#
# Example:
#

age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# ============================================================
# 10. MULTIPLE CONDITIONS
# ============================================================

score = int(input("What was your score? "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# ============================================================
# 11. STRINGS AND IF STATEMENTS
# ============================================================

favorite_color = input("What is your favorite color? ")

if favorite_color == "blue":
    print("Blue is a great color!")


# ============================================================
# 12. NOT EQUAL !=
# ============================================================

password = input("Enter the password: ")

if password != "python123":
    print("That is not the correct password.")


# ============================================================
# 13. BOOLEAN VALUES
# ============================================================
#
# Remember that True and False are boolean values.
#

is_student = True

if is_student:
    print("You are a student.")


# ============================================================
# QUICK SUMMARY
# ============================================================
#
# IF
#
# if condition:
#     code
#
#
# IF / ELSE
#
# if condition:
#     code
# else:
#     other code
#
#
# IF / ELIF / ELSE
#
# if condition:
#     code
# elif another_condition:
#     code
# else:
#     other code
#
# ============================================================