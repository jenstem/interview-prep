# Sorting

# Insertion Sort with Shift Count

# Write a Python program to use insertion sort 
# to sort a list of numbers and count the number of shifts required.


def insertionSort(customList):
    shiftCount = 0
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
            shiftCount += 1
        customList[j + 1] = key

    return customList, shiftCount

cList = [2,1,7,6,5,3,4,9,8]
sorted_numbers, shifts = insertionSort(cList)
print("Sorted List:", sorted_numbers)
print("Number of Shifts:", shifts)