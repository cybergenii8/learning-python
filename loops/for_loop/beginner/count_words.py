# Count Words in a String

# Task: Write a python program that takes a sentence input from the user and counts the number of words using for loop (no using .split())

# Get user input
user_sentence = input("Enter a sentence: ")

# Initialize a variable to store word counts
# use strip to remove any leading and trailing whitespace
# when the user enters an empty string the result is 0 not 1
word_count = 1 if user_sentence.strip() else 0

# Use a for loop to count each word
for char in user_sentence:
    if char == " ":
        word_count += 1


# Display the word counts
print("Number of words: ", word_count)
