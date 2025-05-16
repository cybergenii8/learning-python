# Vowel Counter

# Task: Write a python program that takes a string input from the user and counts the number of vowels (a,e,i,o,u) using for loop.

# Get user input
user_string = input("Enter a text: ")

# Initialize an empty variable to store vowel counts
vowel_count = 0

# Initialize a variable to store vowel
vowel = "aeiouAEIOU"

# Use for loop to count each vowel
for char in user_string:
    if char in vowel:
        vowel_count += 1

# Display the vowel counts
print("Number of vowels:", vowel_count)
