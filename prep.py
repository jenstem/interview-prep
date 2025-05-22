# Searching

# Linear Search

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            print(f"(True, {i})")
            return True
    return print(f"(False, Not found)")

data = ["A", 40, "C", True, 90]
print(linearSearch(data, "D"))
