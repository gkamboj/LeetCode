class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []

        while left < right and top < bottom:
            for ind in range(left, right):
                ans.append(matrix[top][ind])
            top += 1
            
            for ind in range(top, bottom):
                ans.append(matrix[ind][right - 1])
            right -= 1

            if right > left and bottom > top:
                for ind in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][ind])
                bottom -= 1
            
                for ind in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[ind][left])
                left += 1
        
        return ans

'''
Approach: Move right → down → left → up, repeatedly, moving inward layer by layer.
Take care of end indices to avoid index out of bound and missed numbers.
Refer NC iterative solution for more detail.
'''
