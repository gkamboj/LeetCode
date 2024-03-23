class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        start, end = 0, len(s)  - 1
        while start <= end:
            if not s[start].isalpha() and not s[start].isnumeric():
                start += 1
                continue
            if not s[end].isalpha() and not s[end].isnumeric():
                end -= 1
                continue
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True
    