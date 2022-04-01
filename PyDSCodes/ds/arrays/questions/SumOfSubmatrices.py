def findAllSubmatricesSum(matrix):
    ans = 0
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            ans += matrix[row][col] * (row + 1) * (col + 1) * (rows - row) * (cols - col)
    return ans


matrix = [[0, 2, -7, 0],
          [9, 2, -1, 2],
          [-4, 1, -4, 1],
          [-1, 8, 0, -2],
          [3, 5, 8, -2]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(findAllSubmatricesSum(matrix))

# Approach: Multiply each element with the x where x is the number of sub-matrices that element will appear in. To
# find x, observe that mat[i][j] will be part of all sub-matrices which start from any point till [i, j] (including i
# and j) and end after [i, j] (again including i and j). Number of ways if finding start point = (i + 1) * (j + 1)
# because i and j are 0-based indices => number of values till i = (i + 1). Similarly, for end: (m + 1 - (i + 1))
# * (n + 1 - (j + 1_)) = (m - i) * (n - j). So, answer = (i + 1) * (j + 1) * (m - i) * (n - j)
