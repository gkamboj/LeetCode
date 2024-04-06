class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else: stack.append(char)
        return ''.join(stack)
            
''' Approach: Maintain stack of valid chars. While iterating over the string, if current char forms bad pair
with the stack's top, pop from stack; else add to stack.'''
    