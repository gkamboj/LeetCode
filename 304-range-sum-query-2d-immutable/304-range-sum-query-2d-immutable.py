class NumMatrix:

    prefixSumMatrix = []
    
    def __init__(self, matrix: List[List[int]]):
        self.prefixSumMatrix = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        for i in range(1, len(self.prefixSumMatrix)):
            for j in range(1, len(self.prefixSumMatrix[0])):
                self.prefixSumMatrix[i][j] = self.prefixSumMatrix[i - 1][j] + self.prefixSumMatrix[i][j - 1] +  matrix[i - 1][j - 1] - self.prefixSumMatrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSumMatrix[row2 + 1][col2 + 1] - self.prefixSumMatrix[row1][col2 + 1] - self.prefixSumMatrix[row2 + 1][col1] + self.prefixSumMatrix[row1][col1]
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

