class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            row, col = mid//len(matrix[0]), mid % len(matrix[0])
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False