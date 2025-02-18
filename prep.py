# Recursion - capitalizeWords

# Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.

# Examples

# words = ['i', 'am', 'learning', 'recursion']
# capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']

def capitalizeWords(words):
    result = []
    if len(words) == 0:
        return result
    result.append(words[0].upper())
    return result + capitalizeWords(words[1:])    