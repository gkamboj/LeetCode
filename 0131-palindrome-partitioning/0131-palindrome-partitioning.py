class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.helper(s, [], 0, result)
        return result

    def helper(self, s, vals, ind, result):
        if ind == len(s):
            result.append(list(vals))
            return
        
        for i in range(ind, len(s)):
            if self.isPalindrome(s, ind, i):
                vals.append(s[ind : i + 1])
                self.helper(s, vals, i + 1, result)
                vals.pop()
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
