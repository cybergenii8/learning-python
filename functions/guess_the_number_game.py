# Guess the Number Game

# Task: Write a function guess_game(secret) where the user keeps guessing the number until they get it right. Use input() and a while loop.

import random

def guess_game(secret):
    guess = None

    while guess != secret:
        guess = int(input("Gess the number between 1 and 10: "))
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Bingo! You guessed the right number.")

guess_game(7)