# Countdown Timer

# Task: Write a function countdown(n) that prints numbers from n to 0 using a while loop.


def countdown(n):
    """Iterate the numbers from n to 0 and prints

    Args:
        n (int)
    """

    # Use while loop to iterate
    while n >= 0:
        print(n)
        n -= 1


countdown(10)
