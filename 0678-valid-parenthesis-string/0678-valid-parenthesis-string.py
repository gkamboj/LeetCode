class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, star_stack = [], []
        for ind, char in enumerate(s):
            if char == '(':
                stack.append(ind)
            elif char == ')':
                if stack: stack.pop()
                elif star_stack: star_stack.pop()
                else: return False
            else: star_stack.append(ind)
        
        while stack and star_stack and stack[-1] < star_stack[-1]:
            stack.pop()
            star_stack.pop()
        
        return not stack