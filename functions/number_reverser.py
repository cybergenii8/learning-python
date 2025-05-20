# Number Reverser

# Task: Write a function reverse_number(n) that returns the reverse of an integer (e.g.,123 -> 321) using while loop.

def reverse_number(n):
    reverse_number = 0

    while n > 0:
        digit = n % 10
        reverse_number = (reverse_number * 10) + digit
        n //= 10

    return reverse_number

print(reverse_number(123))