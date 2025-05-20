# Sum of Digits

# Create a function sum_digits(n) that returns the sum of the digits of a number using a while loop.

def sum_digits(n):
    sum_of_digits = 0
    
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    
    return sum_of_digits

print(sum_digits(39))