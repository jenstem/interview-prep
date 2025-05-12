# Sorting

# Merge Sort

import math

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))  
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])    
  
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

# helper function
def merge(customList, l, m, r):    
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0    
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1  
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
  
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1



cList = [2,1,7,6,5,3,4,9,8] 
print(bucketSort(cList))     