def findMaxSumSubarray(arr):
    maxSoFar, curr = arr[0], arr[0]
    start, end, tempStart = -1, -1, -1
    for ind, num in enumerate(arr):
        if num > curr + num:
            tempStart = ind
            curr = num
        else:
            curr = curr + num
        if curr > maxSoFar:
            start = tempStart
            end = ind
            maxSoFar = curr
    return [start, end, maxSoFar]


arr = [-2, 1, -3, 4, -1, 2, 1, -3, 4]
arr2 = [5, 4, -1, 7, 8]
print(findMaxSumSubarray(arr))

#Approach: This is Kadane's algorithm. See LC-53 submission for detail.