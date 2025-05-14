# Sorting

# Merge Sort

# Write a Python program to implement merge sort 
# and print the sublists at each merge step.

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

        print(f"Merged: {customList}")            

if __name__ == "__main__":
    customList = [2,1,7,6,5,3,4,9,8] 
    print("Initial array:", customList)
    mergeSort(customList)
    print("Sorted array:", customList)