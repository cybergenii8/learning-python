# Count Words in a String

# Task: Write a python program that takes a sentence input from the user and counts the number of words using for loop (no using .split())

# Get user input
user_sentence = input("Enter a sentence: ")

# Initialize a variable to store word counts
word_count = 1  # set 1 to default

# Use a for loop to count each word
for char in user_sentence:
    if char == " ":
        word_count += 1


# Display the word counts
print("Number of words: ", word_count)
