# Sorting

# Merge Sort

# Write a Python program to apply merge sort on a list 
# of dictionaries based on a specific key

def mergeSort(customList, key):
    if len(customList) > 1:
        m = len(customList) // 2

        L = customList[:m]
        R = customList[m:]

        mergeSort(L, key)
        mergeSort(R, key)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                customList[k] = L[i]
                i += 1
            else:
                customList[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            customList[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            customList[k] = R[j]
            j += 1
            k += 1 
        
data = [
    {'name': 'John', 'age': 75},
    {'name': 'Jane', 'age': 22},
    {'name': 'Dave', 'age': 40}
]      

mergeSort(data, 'age')
print(data)
