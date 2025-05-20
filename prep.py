# Sorting

import time
import random

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_lomuto(arr, low, high):
    if low < high:
        pi = lomuto_partition(arr, low, high)
        quick_sort_lomuto(arr, low, pi - 1)
        quick_sort_lomuto(arr, pi + 1, high)

def quick_sort_hoare(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)

def performance_comparison(size):
    arr_lomuto = [random.randint(1, 1000) for _ in range(size)]
    arr_hoare = arr_lomuto.copy()

    start_time = time.time()
    quick_sort_lomuto(arr_lomuto, 0, len(arr_lomuto) - 1)
    lomuto_time = time.time() - start_time

    start_time = time.time()
    quick_sort_hoare(arr_hoare, 0, len(arr_hoare) - 1)
    hoare_time = time.time() - start_time

    print(f"Lomuto Quick Sort Time: {lomuto_time:.6f} seconds")
    print(f"Hoare Quick Sort Time: {hoare_time:.6f} seconds")


performance_comparison(1000)