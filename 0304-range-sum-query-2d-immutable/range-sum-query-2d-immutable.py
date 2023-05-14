class NumMatrix:

    prefixSumMatrix = []
    
    def __init__(self, matrix: List[List[int]]):
        self.prefixSumMatrix = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        for row in range(1, len(self.prefixSumMatrix)):
            for col in range(1, len(self.prefixSumMatrix[0])):
                self.prefixSumMatrix[row][col] = self.prefixSumMatrix[row][col - 1] + self.prefixSumMatrix[row - 1][col] + matrix[row - 1][col - 1] - self.prefixSumMatrix[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSumMatrix[row2 + 1][col2 + 1] - self.prefixSumMatrix[row1][col2 + 1] - self.prefixSumMatrix[row2 + 1][col1] + self.prefixSumMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#Approach: Since there are multiple queries, we should create an auxiliary cache storage to avoid doing similar calculation again. prefixSumMatrix is that storage which is storing the sum of all elements of matrix upto given element. This allows to fetch the sum between any two set of indices in O(1).
