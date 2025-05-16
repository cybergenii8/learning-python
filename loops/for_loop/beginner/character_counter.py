# Character Counter

# Task: Write a python program that takes a string (text) input from the user and counts the occurences of each character using a for loop.

# Get user input
user_string = input("Enter a text: ")

# Initialize an empty dictionary to store character counts
char_count = {}

# Use for loop to count each character
for char in user_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the character counts
print("character counts:")
for char, count in char_count.items():
    print(f"{char}: {count}")
