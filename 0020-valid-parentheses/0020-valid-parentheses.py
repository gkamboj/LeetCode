class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[':']', '{':'}', '(':')'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif i in brackets.values():
                if not stack or brackets[stack.pop()] != i:
                    return False
            else:
                return False
        return False if stack else True