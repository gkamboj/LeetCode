def findMaxSumSubarray(arr):
    maxSoFar, curr = arr[0], arr[0]
    start, end, tempStart = 0, 0, 0
    for ind, num in enumerate(arr[1:]):
        if num > curr + num:
            tempStart = ind
            curr = num
        else:
            curr = curr + num
        if curr > maxSoFar:
            start = tempStart
            end = ind
            maxSoFar = curr
    return [start + 1, end + 1, maxSoFar] # Incrementing start and end by 1 because for loop was starting from 1st
    # index i.e. for every ind, actual index is (ind + 1)


arr = [-2, 1, -3, 4, -1, 2, 1, -3, 4]
arr2 = [5, 4, -1, 7, 8]
print(findMaxSumSubarray(arr))
