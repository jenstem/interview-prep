# Searching

# Binary Search  

import math

def binarySearch(array, value, tolerance=1e-9):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) // 2)
    
    while start <= end:
        if abs(array[middle] - value) <= tolerance:
            return middle
        elif value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) // 2)
    
    return -1    
 

custArray = [8.1, 9.1, 12.1, 15.1, 17.1, 19.1, 20.1, 21.1, 28.1]
print(binarySearch(custArray, 12.1))