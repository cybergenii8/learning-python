# Factorial Calculator

# Task: Write a function factorial(n) that calculates the factorial of a number using while loop

def factorial(n):
    counter = 1
    factorial = 1

    while counter <= n:
        factorial *= counter
        counter += 1
    
    print(f"Factorial number of {n} is {factorial}")

factorial(5)