# Given an array of integers A, sort the array into a wave like array and return it, In other words, arrange the
# elements into a sequence such that
# a1 >= a2 <= a3 >= a4 <= a5….
# Note: If there are multiple answers possible, return the one that's lexicographically smallest.

def waveArray(arr):
    arr.sort()
    for ind in range(0, (len(arr) // 2) * 2, 2):
        arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
    return arr


arr = [5, 9, 3, 8, 11, 1, 4, 13, 12]
arr2 = [7, 11, 6, -66, 23, 56, 99, -12, 0, 10]
print(waveArray(arr2))

# Approach: Sort the array and swap adjacent elements in pairs. Remember to handle even-odd length array cases.
