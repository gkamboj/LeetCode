class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s)  - 1
        while start <= end:
            if not s[start].isalpha() and not s[start].isnumeric():
                start += 1
            elif not s[end].isalpha() and not s[end].isnumeric():
                end -= 1
            elif s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
    
# Approach: Change the string to lower, and check for palindrome along with conditions of the question.
    
