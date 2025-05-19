# Counting Word Frequencies

# Task : Write a python program that takes a sentence from user input and count the frequency of each word using a for loop.

# Get the user input
user_sentence = input("Enter a sentence: ")

# Initialize an empty dictionaries to store word counts
word_count = {}

# Initialeze a variable to store every word from user input
list_word = user_sentence.split()

# Use for loop to count each word
for word in list_word:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    
# Display the word counts
print("Word counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")
