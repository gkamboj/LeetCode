class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []
        
        
        def backtrack(openP, closeP):
            if len(stack) == 2*n:
                result.append(''.join(stack))
                
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
                
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result
        