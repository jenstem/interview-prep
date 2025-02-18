# Recursion - capitalizeFirst

# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

# Example

# capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])