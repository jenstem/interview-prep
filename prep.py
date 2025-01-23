# Recursion - Factorial

# Write a function which accepts a number and returns the factorial of that number.
# A factorial is the product of an integer and all the integers below it; e.g.
# factorial four (4!) is equal to 4*3*2*1 = 24.
# factorial of zero (0!) is always 1.

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(7))