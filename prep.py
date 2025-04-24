# Sorting

# Bubble Sort

# Relative Sort Array #1122

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items 
# in arr1 are the same as in arr2. Elements that do not appear in arr2 
# should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = {num: 0 for num in arr1}
        for num in arr1:
            arr1_count[num] += 1

        result = []
        for num in arr2:
            result.extend([num] * arr1_count[num])
            arr1_count[num] = 0

        remaining = []
        for num in arr1_count:
            remaining.extend([num] * arr1_count[num])
        result.extend(sorted(remaining))
        return result