class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) * len(matrix[0]) - 1
        colSize = len(matrix[0])
        ans = False
        while low <= high:
            mid = (high - low) // 2 + low
            if matrix[mid // colSize][mid % colSize] == target:
                ans = True
                break
            elif matrix[mid // colSize][mid % colSize] > target:
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
