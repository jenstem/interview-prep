# Searching

# Binary Search  

import math

def binarySearch(array, value, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start > end:
        return -1
    middle = (start + end) // 2
    if array[middle] == value:
        return middle
    elif value < array[middle]:
        return binarySearch(array, value, start, middle - 1)
    else:
        return binarySearch(array, value, middle + 1, end)     
 

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 12))