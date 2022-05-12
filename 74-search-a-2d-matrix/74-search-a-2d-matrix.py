class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            val = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if target == val:
                return True
            elif target > val:
                start = mid + 1
            else:
                end = mid - 1
        return False