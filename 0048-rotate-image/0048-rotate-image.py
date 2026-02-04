class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                top, bottom = matrix[i][j], matrix[n-i-1][n-j-1]
                if self.isProcessed(top):
                    continue
                right, left = matrix[j][n-i-1], matrix[n-j-1][i]
                matrix[i][j] = self.formatValue(left)
                matrix[j][n-i-1] = self.formatValue(top)
                matrix[n-i-1][n-j-1] = self.formatValue(right)
                matrix[n-j-1][i] = self.formatValue(bottom)
        
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



                