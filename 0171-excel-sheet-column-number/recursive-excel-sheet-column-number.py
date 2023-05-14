class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = [0]
        self.solve(0, columnTitle, ans)
        return ans[0]
    
    def solve(self, i, column, ans):
        if i == len(column):
            return
        ans[0] += (ord(column[-i-1]) - ord('A') + 1) * (26 ** i)
        self.solve(i + 1, column, ans)
        
    
# Approach: This is recursive approach with logic similar to iterative sumbission.
