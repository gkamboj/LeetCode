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
        elif len(s) <= 1:
            d[s] = True
            result = d[s]
        else:
            if s[0] != s[-1]:
                d[s] = False
                result = d[s]
            else:
                result = self.isPalindrome(s[1:-1], d)
        return result
    
# Approach: This is backtracking approach using DFS. To optimise the isPalindrome method, dictionary is used to store the result of already checked strings. Refer Approach-2 of LC official solution for detail.
