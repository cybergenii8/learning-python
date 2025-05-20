# Factorial Calculator

# Task: Write a function factorial(n) that calculates the factorial of a number using while loop


def factorial(n):
    """Return factorial from n

    Args:
        n (_int_)
    """

    # Initialize a variable to store the factorial result
    factorial = 1

    # Use while loop to get the numbers
    while n > 1:
        factorial *= n
        n -= 1

    return factorial


print(factorial(10))
