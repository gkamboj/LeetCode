# Given an array of integers A of size N that is a permutation of [0, 1, 2, …, (N-1)].
# Rearrange the array such that A[i] = j is changed to A[j] = i for all i and j form 0 to N-1.

def rearrangeArray(arr):
    n = len(arr)
    for ind in range(n):
        arr[arr[ind] % n] += n * ind
    for ind in range(n):
        arr[ind] = arr[ind] // n
    return arr


def rearrangeArray2(arr):
    n = len(arr)
    for i in range(n):
        arr[i] *= n
    for i in range(n):
        arr[arr[i] // n] = arr[arr[i] // n] * n + i
    for i in range(n):
        arr[i] %= n
    return arr


arr = [2, 0, 1, 4, 5, 3]
arr2 = arr[:]
# 1 2 0 5 3 4
print(rearrangeArray(arr))
print(rearrangeArray2(arr2))

# Approach-1: The idea is to store each element’s new and old value as quotient and remainder of n, respectively (n
# being the size of the array). Instead of using arr[arr[ind]] in line-7, arr[arr[ind] % n] is used because some of
# the elements maybe having the updated value when we reach that ind and accessing arr[arr[ind]] will give index out
# of bound exception.

# Approach-2: Similar to first approach, but here the ans is stored as remainder instead of quotient.
