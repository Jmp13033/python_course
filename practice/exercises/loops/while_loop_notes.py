"""
===========================================
🐍 Python While Loops - Lesson Notes 🐍
===========================================

A while loop repeats code WHILE a condition
is True.

Example:

while condition:
    do something

Be careful!

If the condition never becomes False,
the loop can run forever!
"""


# ==========================================
# Example 1 - A Simple While Loop
# ==========================================

print("Example 1")

number = 1

while number <= 5:
    print(number)
    number = number + 1


# The loop works like this:
#
# number = 1
# Is 1 <= 5? YES → print 1
#
# number = 2
# Is 2 <= 5? YES → print 2
#
# ...
#
# number = 6
# Is 6 <= 5? NO → stop!


# ==========================================
# Example 2 - Counting Down
# ==========================================

print("\nExample 2")

number = 5

while number > 0:
    print(number)
    number = number - 1

print("Blast off! 🚀")


# ==========================================
# Example 3 - Using a Variable
# ==========================================

print("\nExample 3")

health = 100

while health > 0:
    print("Health:", health)
    health = health - 20

print("Game Over!")


# ==========================================
# Example 4 - While + Input
# ==========================================

print("\nExample 4")

answer = ""

while answer != "yes":
    answer = input("Are you ready? ")

print("Let's go!")


# ==========================================
# Example 5 - Guessing Game
# ==========================================

print("\nExample 5")

secret_number = 7

guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

print("You got it! 🎉")


# ==========================================
# Example 6 - Using if Inside a While Loop
# ==========================================

print("\nExample 6")

number = 1

while number <= 10:

    if number == 5:
        print("We found 5!")

    else:
        print(number)

    number = number + 1


# ==========================================
# Example 7 - A Game Loop
# ==========================================

print("\nExample 7")

playing = "yes"

while playing == "yes":

    print("🎮 Playing the game...")

    playing = input("Do you want to keep playing? ")

print("Thanks for playing!")


# ==========================================
# for vs while
# ==========================================

"""
FOR LOOP

Use a for loop when you want to go through
a list or repeat something a known number
of times.

Example:
"""

for number in range(5):
    print(number)


"""
WHILE LOOP

Use a while loop when you want to keep
doing something while a condition is True.

Example:
"""

number = 0

while number < 5:
    print(number)
    number = number + 1


# ==========================================
# ⚠️ IMPORTANT: Infinite Loops
# ==========================================

"""
Be careful!

This loop NEVER stops:

    number = 1

    while number <= 5:
        print(number)

Why?

Because number never changes.

The condition will ALWAYS be True.

Always make sure something inside your
while loop can eventually make the
condition False.
"""


# ==========================================
# Summary
# ==========================================

"""
✔ while loops repeat while something is True

✔ Conditions control when the loop stops

✔ Variables can change inside the loop

✔ input() works really well with while loops

✔ while loops are great for games!

✔ Be careful of infinite loops

Great job! 🎉
"""