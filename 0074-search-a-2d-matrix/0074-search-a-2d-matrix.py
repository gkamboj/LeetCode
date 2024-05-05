class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)*len(matrix[0]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            row, col = mid//len(matrix[0]), mid%len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
    
'''
Approach: treat 2D array as 1D array by considering its lenth as m * n and apply binary search.
'''