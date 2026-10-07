import random

# Choose a random number between 1 and 100
secret_number = random.randint(1, 100)

# Keep track of attempts
attempts = 0

print("I'm thinking of a number between 1 and 100!")

# Keep asking until the player guesses correctly
while True:

    # Ask the player for a guess
    guess = int(input("Enter your guess: "))

    # Increase the number of attempts
    attempts += 1

    # TODO: Check if the guess is too low

    # TODO: Check if the guess is too high

    # TODO: Check if the guess is correct