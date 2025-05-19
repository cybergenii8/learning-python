# Removing Duplicate Characters

# Task: Write a python program that takes a word from the user input and removes all duplicate characters in a string using a for loop.

# Get the user input
user_string = input("Enter a word: ")

# Initialize a variable to store the result
result = " "

for char in user_string:
    if char not in result:
        result += char


print(result)
