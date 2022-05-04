class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.palindromePartitioning(s, [], result)
        return result
        
    def palindromePartitioning(self, s, curr, result):
        if not s:
            result.append(curr)
            return
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.palindromePartitioning(s[i+1:], curr + [s[:i+1]], result)
            
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True
    
# Approach: This is backtracking approach using DFS. Refer approach-1 of LC official solution for detail.
