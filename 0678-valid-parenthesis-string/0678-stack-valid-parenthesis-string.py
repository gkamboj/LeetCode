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
    
'''
Approach: Maintain 2 stacks: each to store indices of open brackets and stars. Travers the string, and if both 
stacks are empty on encountering closed bracket, return False as this mean counting all stars as open brackets 
is also not enough for balancing closed brackets. After traversal, if all open brackets cannot be balanced by
stars (compare indices for balance feasibility check), return False.

Note: Do check approch-4 and https://leetcode.com/problems/valid-parenthesis-string/solution/2338165 for
solution with no extra space.
'''    
