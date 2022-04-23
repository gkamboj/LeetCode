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
    
# Approach: Since the first element of row is greater than the last element of previous row, whole matrix can be treated as a 1-D sorted matrix. So, considering the given matrix as 1-D sorted matrix, we can apply the binary serach algorithm.

# Note: Since there is no comparison with adjacent elements in main method, minMat <= maxMat is used (and not minMat < maxMat).
