# Sorting

# Merge Sort

# Write a Python script to sort a list using merge sort and count 
# the total number of comparisons made during the merge process.

def mergeSort(customList):
    if len(customList) > 1:
        m = len(customList) // 2

        L = customList[:m]
        R = customList[m:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        comparisons = 0

        while i < len(L) and j < len(R):
            comparisons += 1
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
        return comparisons
    return 0           

def sort_and_count(customList):
    total_comparisons = mergeSort(customList)
    return customList, total_comparisons        

if __name__ == "__main__":
    customList = [2,1,7,6,5,3,4,9,8] 
    sortedList, total_comparisons = sort_and_count(customList)
    print("Sorted array:", sortedList)
    print("Total comparisons made:", total_comparisons)
