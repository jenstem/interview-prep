# Sorting

# Heap Sort

def heapify(customList, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and customList[l][key] < customList[largest][key]:
        largest = l

    if r < n and customList[r][key] < customList[largest][key]:
        largest = r     
 
    if largest != i:
        customList[i], customList[largest] = customList[largest], customList[i]
        heapify(customList, n, largest, key)

def heapSort(customList, key):
    n = len(customList)

    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i, key)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0, key)
  

if __name__ == "__main__":
    data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
    heapSort(data, 0)
    print(data)