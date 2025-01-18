# Recursion - Power

# How to calculate power of a number using recursion?


def power(base, exp):
    assert int(exp) == exp, 'The exponent must be an integer number only'
    if exp == 0:
        return 1
    return base * power(base, exp-1)

print(power(4,5))