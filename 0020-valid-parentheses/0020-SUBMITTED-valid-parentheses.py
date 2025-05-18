class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
            }
        stack = []
        for b in s:
            if b in chars:
                stack.append(b)
            elif not stack or chars[stack.pop()] != b:
                return False
        return not stack

# Approach: Use dictionary to store brackets and stack for LIFO.
