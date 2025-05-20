# Sorting

def quick_sort(arr, low, high, depth=0):
    if low < high:
        pi, current_depth = partition(arr, low, high, depth)
        depth = max(depth, current_depth)
        depth = quick_sort(arr, low, pi - 1, depth)
        depth = quick_sort(arr, pi + 1, high, depth)
    return depth

def partition(arr, low, high, depth):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, depth + 1

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    recursion_depth = quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)
    print("Recursion depth:", recursion_depth)