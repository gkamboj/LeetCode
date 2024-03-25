class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(openP, closeP, path):
            if len(path) == 2*n:
                result.append(path)
                
            if openP < n:
                backtrack(openP + 1, closeP, path + "(")
                
            if closeP < openP:
                backtrack(openP, closeP + 1, path + ")")
        
        backtrack(0, 0, "")
        return result
        
# Approach:
# 1. Add open bracket if open bracket count < n
# 2. Add closed bracket if closed bracket count < open count
# 3. Add to result if path size = 2n
# Similar to stack solution submission, but using string instead of stack.
# Detail: https://www.youtube.com/watch?v=s9fokUqJ76A
