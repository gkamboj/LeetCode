class Solution:
    def maxDepth(self, s: str) -> int:
        ans, count = 0, 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            ans = max(ans, count)
        return ans
    
''' Approach: Given that input is VPS, we don't need to check for the validity of the input string. So, this
can be done without using extra space of stack (needed for checking the if input is VPS) '''
