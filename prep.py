# Sorting

# Bucket Sort

import math

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets

    buckets = [[] for _ in range(numberofBuckets)]

    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)

    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i].sort()
        sorted_array += buckets[i]

    return sorted_array

cList = [2,1,7,6,5,3,4,9,8] 
print(bucketSort(cList))   