# Counting Vowels and Consonants

# Task : Write a python program that takes a string input from user and counts the number of vowels and consonants in it using a for loop

# Get user input
user_string = input("Enter a word: ")

# Initialize an empty variable to store vowel and consonant counts
vowel_count = 0
consonant_count = 0
# Initialize a variable to store vowel
vowel = 'aiueoAIUEO'

for char in user_string:
    if char in vowel:
        vowel_count += 1
    else:
        consonant_count += 1

# Display the result
print(f"In this word '{user_string}' there is {vowel_count} vowels and {consonant_count} consonants.")