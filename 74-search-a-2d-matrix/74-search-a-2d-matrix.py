class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while low < high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return matrix[low // cols][low % cols] == target
    
#Approach: This is binary search approach. Treat 2-D array as 1-D and apply binary search approach. Remember few conditions:
#1. use low < high (not low != high -> this will be issue if high becomes lesser than low)
#2. While returning, check if current element is same as target to handle cases like input -> [[1]], 1

#See other submissions for alternate approaches