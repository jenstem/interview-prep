# Searching

# Linear Search

def linearSearch(arr, target):
    iterations = 0
    for index, value in enumerate(arr):
        iterations += 1
        if value == target:
            print(f"Iteration {iterations}: {value}")
            return index
    print(f"Target not found after {iterations} iterations.")
    return -1        

data = ["A", 40, "C", True, 90]
print(linearSearch(data, 40))
