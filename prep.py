# Sorting

# Heap Sort

def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and customList[l] < customList[smallest]:
        smallest = l

    if r < n and customList[r] < customList[smallest]:
        smallest = r     
 
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)