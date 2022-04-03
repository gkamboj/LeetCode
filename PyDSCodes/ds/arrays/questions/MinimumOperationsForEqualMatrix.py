# Minimum operations of given type to make all elements of a matrix equal

# Given a matrix of integers A of size N x M and an integer n. In a single operation, B can be added to or subtracted
# from any element of the matrix. Find and return the minimum number of operations required to make all the elements
# of the matrix equal and if it is impossible return -1 instead.

def findMinOperations(matrix, num):
    arr = []
    mod = matrix[0][0] % num

    for row in matrix:
        for col in row:
            if col % num != mod:
                return -1
            arr.append(col)

    arr.sort()
    size = len(arr)

    median = arr[size // 2]
    ans = 0

    for val in arr:
        ans += abs(val - median) // num

    if len(arr) % 2 == 0:
        ans2 = 0
        median2 = arr[size // 2 - 1]
        for val in arr:
            ans2 += abs(val - median2) // num
        ans = min(ans, ans2)

    return ans


matrix = [[0, 2, 8],
          [8, 2, 0],
          [0, 2, 8]]
n = 2

matrix2 = [[2, 4, 6],
           [8, 10, 12],
           [14, 16, 18],
           [20, 22, 24]]
print(findMinOperations(matrix2, n))

# Approach: All the elements can be made equal only if every element returns same remainder on dividing with given
# number n. If the remainder is same, sort all the elements using an auxiliary array. Now observe that for minimum
# operations, every number should be made equal to median of thi array. If array size is even, then consider both
# medians and consider the case giving lower operations count.
