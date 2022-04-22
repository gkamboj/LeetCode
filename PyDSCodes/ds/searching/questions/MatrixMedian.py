# Given a matrix of integers A of size N x M in which each row is sorted. Find and return the overall median of
# matrix A. Note that no extra space is allowed.

def matrixMedian(matrix):
    minMat, maxMat = matrix[0][0], matrix[0][-1]
    reqCount = 1 + len(matrix) * len(matrix[0]) // 2
    for i in matrix:
        minMat = min(i[0], minMat)
        maxMat = max(i[-1], maxMat)
    while minMat <= maxMat:
        mid = minMat + (maxMat - minMat) // 2
        count = 0
        for arr in matrix:
            count += countLessThanX(arr, mid)
        if count >= reqCount:
            maxMat = mid - 1
        else:
            minMat = mid + 1
    return minMat


def countLessThanX(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= x:
            low = mid + 1
            # Using (mid + 1) because array is 0 index based. If mid-index is answer then count will be (mid + 1)
        else:
            high = mid - 1
    return low


matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]
print(matrixMedian(matrix))

# Approach: Find the minimum and maximum value in matrix. Now apply binary search using these 2 values: For the
# middle value, check if count of elements less than or equal to this middle element is >= required count (required
# count = count for the median, that is number of elements which should be less than median).

# Note-1: There is no if condition for == condition in main method. This is because even if get count same as
# requiredCount, we cannot be sure that mid is part of matrix. So we continue loop till it's ended by terminating
# condition.

# Note-2: Since there is no comparison with adjacent elements in main method, minMat <= maxMat is used (and not
# minMat < maxMat).

# Note-3: Observe that count >= reqCount is used in main method (and not count > reqCount).

# Note-4: In method countLessThanX, since we're not doing comparison with any adjacent element,
# we should use low <= high & igh = mid - 1.
