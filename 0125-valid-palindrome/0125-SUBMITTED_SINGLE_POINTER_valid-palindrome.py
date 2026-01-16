class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = ''
        for char in s.lower():
            if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            # if char.isalpha() or char.isnumeric():
                alpha_str += char
        
        for ind in range(len(alpha_str) - 1//2):
            if alpha_str[ind] != alpha_str[-1*ind -1]:
                return False

        return True
