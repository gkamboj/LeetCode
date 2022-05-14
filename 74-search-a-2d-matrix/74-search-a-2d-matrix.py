class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            val = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if val == target:
                return True
            elif val > target:
                end = mid - 1
            else:
                start = mid + 1
        return False