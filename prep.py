# Recursion

def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    print("I am the fourth method")

firstMethod()