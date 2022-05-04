class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        dp = {}
        self.palindromePartitioning(s, [], result, dp)
        return result
        
    def palindromePartitioning(self, s, curr, result, dp):
        if not s:
            result.append(curr)
            return
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1], dp):
                self.palindromePartitioning(s[i+1:], curr + [s[:i+1]], result, dp)
            
    def isPalindrome(self, s, d):
        if s in d:
            result = d[s]
        else:
            d[s] = True
            for i in range(len(s) // 2):
                if s[i] != s[-i-1]:
                    d[s] = False
                    break
            result = d[s]
        return d[s]
    
# Approach: This is backtracking approach using DFS. Refer approach-1 of LC official solution for detail.