class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, ans = [], []

        def helper(open, close):
            if len(stack) == 2*n:
                ans.append(''.join(stack))
            
            if open < n:
                stack.append('(')
                helper(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(')')
                helper(open, close + 1)
                stack.pop()
            
        helper(0, 0)
        return ans
            
