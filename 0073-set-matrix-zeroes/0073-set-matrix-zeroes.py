class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use 0-th row and column as marker
        col0_has_zero = False
        row0_has_zero = 0 in matrix[0]
        for c in range(len(matrix)):
            if not matrix[c][0]:
                col0_has_zero = True
                break
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if not matrix[r][c]:
                    matrix[0][c] = 0 #c-th col has zero
                    matrix[r][0] = 0 #r-th row has zero

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if not matrix[r][0] or not matrix[0][c]: # Set to zero if r-th row or c-th col has zero
                    matrix[r][c] = 0

        # set 0-th row and column
        if row0_has_zero:
            matrix[0] = [0 for c in range(len(matrix[0]))]
        if col0_has_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0

# Approach: In order, follow:
# (1) Use 0th row and column as marker to store if other rows and columns have zero.
# (2) Iterate again to set non-zero indexed row and column cells to zero.
# (3) Use marker variables to update 0-th row and column.
# This approach allows solving without extra space.