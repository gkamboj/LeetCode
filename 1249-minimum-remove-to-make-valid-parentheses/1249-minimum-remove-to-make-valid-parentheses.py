class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, ls = [], list(s)
        for ind, val in enumerate(ls):
            if val == '(':
                stack.append(ind)
            elif val == ')':
                if stack: stack.pop()
                else: ls[ind] = ''
        while stack: ls[stack.pop()] = ''
        return ''.join(ls)
    
''' Approach: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
'''    