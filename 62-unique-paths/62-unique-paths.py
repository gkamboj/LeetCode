class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
                    
    
# Aproach: This is recursive approach -> Number of ways of reaching the bottom right corner will be the sum of number of ways for reaching left and top of the bottom right cell. Applying this recursively with base case being when m = n = 1.