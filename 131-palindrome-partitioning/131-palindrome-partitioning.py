class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, result, [])
        return result
    
    def dfs(self, s, result, part):
        if not s:
            result.append(part)
            return
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.dfs(s[i+1:], result, part + [s[:i+1]])
        
    
    
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True