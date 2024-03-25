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
        
# Approach:
# 1. Add open bracket if open bracket count < n
# 2. Add closed bracket if closed bracket count < open count
# 3. Add to result if stack size = 2n
# Pop from stack after because same stack variable is not a paramter to the backtrack
# method, same variable is used for other operations.
# Detail: https://www.youtube.com/watch?v=s9fokUqJ76A