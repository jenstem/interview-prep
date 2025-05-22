# Searching

# Linear Search

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            print(f"Found {value} at index {i}")
            return i
    return -1

data = [20, 40, 30, 50, 90]
print(linearSearch(data, 100))
