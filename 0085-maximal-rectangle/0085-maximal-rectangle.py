class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        row_ht, ans = [0 for i in range(len(matrix[0]) + 1)], 0
        
        for row in matrix:
            for ind, ht in enumerate(row):
                if ht != "0": row_ht[ind] += int(ht)
                else: row_ht[ind] = 0
            print(row_ht)
            ans = max(ans, self.maxRectangleArea(row_ht))
            
        return ans
    
    def maxRectangleArea(self, arr):
        stack, ans = [], 0
        for ind in range(len(arr)):
            while stack and arr[stack[-1]] > arr[ind]:
                height = arr[stack.pop()]
                width = ind if not stack else ind - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(ind)
        return ans
    
''' Approach: This is similar to LC-84 (largest rectangle in histogram). Treat every row as a separate 
histogram and find the maximum area. Histogram array can be created by adding he current row values to the 
existing array.
'''