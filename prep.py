# Hashing

def mod(number, cellNumber):
    return number % cellNumber

mod(400, 24)    
mod(700, 24)   


# ASCII function

def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

modASCII("ABC", 24) 