import math 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        for ind, val in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > val:
                last_height = heights[stack.pop()]
                width = ind if not stack else ind - stack[-1] - 1
                ans = max(ans, last_height * width)
            stack.append(ind)
        return ans
    
# Approach: Using stack, refer https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained    