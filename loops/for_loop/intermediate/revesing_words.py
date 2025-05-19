# Reversing Words in a Sentence

# Task: Write a python program that takes a sentence input from the user and reverse the order of the world using a for loop.

# Get user input
user_sentence = input("Enter a sentence: ")

# Initialize a variable for store list words
words = user_sentence.split(" ")

# Initialize a variable for store reversed words
reversed_words = " "

for char in words:
    reversed_words = char + " " + reversed_words

print(reversed_words)