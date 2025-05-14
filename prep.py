# Sorting

# Merge Sort

# Write a Python function to perform merge sort recursively 
# and then verify its stability on a list with duplicate values.

def mergeSort(customList):
    if len(customList) > 1:
        m = len(customList) // 2

        L = customList[:m]
        R = customList[m:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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
        
def is_stable(original, sorted_arr):
    org_indices = {value: [] for value in original}
    for index, value in enumerate(original):
        org_indices[value].append(index)

    sorted_indices = []
    for value in sorted_arr:
        sorted_indices.append(org_indices[value].pop(0))

    return sorted_indices == sorted(sorted_indices)     

customList = [38, 27, 43, 38, 9, 82, 10, 27]
sorted_arr = customList.copy()
mergeSort(sorted_arr)
print("Sorted array is:", sorted_arr)
print("Is stable?", is_stable(customList, sorted_arr))
