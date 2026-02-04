class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                top = matrix[i][j]
                if self.isProcessed(top):
                    continue
                matrix[i][j] = self.formatValue(matrix[n-j-1][i]) # left set to top
                matrix[n-j-1][i] = self.formatValue(matrix[n-i-1][n-j-1]) # bottom set to left
                matrix[n-i-1][n-j-1] = self.formatValue(matrix[j][n-i-1]) # right set to bottom
                matrix[j][n-i-1] = self.formatValue(top) # top set to right
        
        for row in matrix:
            for ind, val in enumerate(row):
                row[ind] = self.fetchValue(val)

    def isProcessed(self, value):
        return True if abs(value) > 1000 else False

    def formatValue(self, value):
        if value < 0:
            return value - 1001
        else:
            return value + 1001

    def fetchValue(self, value):
        if value < 0:
            return value + 1001
        else:
            return value - 1001

# Approach: Find top, right, bottom, and left. Rotate these four by 90 degrees. Repeat the same for every cell.
# Avoid the repitition by storing the value as: val + 1001 for positives (as maximum allowed is 1000) and val - 1000 for negatives.
# Reset the value by adjusting 1001 factor at end.

# Check NeetCode solution for similar approach without needing values adjustment plus another approach using transpose.