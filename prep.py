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

# Direct Chaining

class DirectChaining:
    def __init__(self, cellNumber):
        self.cellNumber = cellNumber
        self.table = [[] for _ in range(cellNumber)]

    def hash_function(self, key):
        return hash(key) % self.cellNumber

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)    