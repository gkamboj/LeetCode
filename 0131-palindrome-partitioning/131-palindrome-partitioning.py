from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, d = [], defaultdict(int)
        self.solve(d, s, result, [])
        return result
    
    def solve(self, d, s, result, pal):
        if not s:
            result.append(pal)
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1], d):
                self.solve(d, s[i + 1:], result, pal + [s[:i+1]])
    
    def isPalindrome(self, s, d):
        if s in d:
            result = d[s]
        elif len(s) <= 1:
            d[s] = True
            result = True
        else:
            if s[0] == s[-1]:
                result = self.isPalindrome(s[1:-1], d)
            else:
                result = False
        d[s] = result
        return result
            