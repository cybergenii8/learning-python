# Remove Vowels from String

# Task: Write a python program that takes a string input from the user and removes all vowels using a for loop.

# Get user input
user_string = input("Enter a text: ")

# Initialize an empty variable to store text after remove all vowel
removed_vowel = ""

# Initialize a variable to store vowel
vowel = "aiueoAIUEO"

# Use for loop to remove vowel
for char in user_string:
    if char not in vowel:
        removed_vowel += char

print(f"{user_string} after the vowel is removed: {removed_vowel}")
