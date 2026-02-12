class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0_has_zero = False
        row0_has_zero = 0 in matrix[0]
        for i in range(len(matrix)):
            if not matrix[i][0]:
                col0_has_zero = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][j]:
                    matrix[0][j] = 0 #j-th col has zero
                    matrix[i][0] = 0 #i-th row has zero

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if row0_has_zero:
            matrix[0] = [0 for i in range(len(matrix[0]))]
        if col0_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0