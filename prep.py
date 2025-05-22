# Searching

# Linear Search

def linearSearch(arr, target):
    n = len(arr)
    halfsies = n // 2

    for i in range(halfsies):
        if arr[i] == target:
            return i
    return -1             

arr = [50, 40, 30, 100, 90, 80]
target = 40
result = linearSearch(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print(f"Element not found in first half of array")    
