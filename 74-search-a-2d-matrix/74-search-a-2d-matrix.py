class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                for num in row:
                    if num == target:
                        return True
        return False