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
