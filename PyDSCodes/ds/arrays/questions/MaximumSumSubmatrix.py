# Find submatrix with maximum sum

def maximumSumSubmatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    topLeftRow, topLeftCol, bottomRightCol, bottomRightRow = 0, 0, 0, 0
    ans = matrix[0][0]
    for upperRow in range(rows):
        temp = [0 for i in range(cols)]
        for lowerRow in range(upperRow, rows):
            for ind in range(cols):
                temp[ind] += matrix[lowerRow][ind]
            maxRowSum, start, end = kadane(temp)
            if maxRowSum > ans:
                topLeftRow = upperRow
                bottomRightRow = lowerRow
                topLeftCol = start
                bottomRightCol = end
                ans = maxRowSum
    return [ans, (topLeftRow, topLeftCol), (bottomRightRow, bottomRightCol)]


def kadane(arr):
    ans, curr = arr[0], arr[0]
    start, end, temp = -1, -1, -1
    for ind, num in enumerate(arr[1:]):
        if num > curr + num:
            curr = num
            temp = ind
        else:
            curr = num + curr
        if curr > ans:
            start = temp
            end = ind
            ans = curr
    return [ans, start + 1, end + 1]


matrix = [[0, 2, -7, 0],
          [9, 2, -1, 2],
          [-4, 1, -4, 1],
          [-1, 8, 0, -2],
          [3, 5, 8, -2]]
print(maximumSumSubmatrix(matrix))

# Approach: Go either row-wise or column-wise. In this case, it's row-wise. For evry possible pair of (i, j) where i
# and j represent rows index s.t. j >= i, find cumulative sum in an array. Using Kadane's, find max sum of this
# array. Accordingly keep updating indexes for start and end of matrix. See https://youtu.be/yCQN096CwWM for details.
