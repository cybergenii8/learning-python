# Caesar Cipher (Simple Encryption)

# Task : Write a python program that takes a word input from the user and implement a caesar chiper using a for loop, which shifts each letter in a string by a specified number of positions.

# import string module to generate alphabets
import string

# Get the user input
user_string = input("Enter a word: ")
user_shift = int(input("Enter a number to shift the letter: "))

# Initialize a variable to store all alphabet ( a-z, A-Z ) 
alphabets = string.ascii_letters

# Initialize a variable to store shifted string
shifted_string = " "

# Initialize a variable to store index
char_index = []

# Use for loop to get index for every character from user input
for char in user_string:
    char_index.append(alphabets.index(char))

# Use for loop to store every character to shifted string
for i in char_index:
    shifted_string = shifted_string + alphabets[i + user_shift]

# Display the result
print(f"{user_string} word after shifting {user_shift} becomes {shifted_string}")