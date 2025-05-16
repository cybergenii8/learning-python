# Reverse A String

# Task: Write a python program that takes a string input from the user and prints the string in reverse order using a for loop.

# Get user input
user_string = input("Enter a text: ")

# Initialize an empty variable to store reverse string
reversed_string = ""

for char in user_string:
    reversed_string = (
        char + reversed_string
    )  # Add each character to the front of reversed string

# Display the reversed string
print(f"The reversed text is: {reversed_string}")
