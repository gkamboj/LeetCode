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
                    
    
# Aproach: This is DP approach using a 2-D array s.t. dp[i][j] represents the number of ways of reching (i, j) from start. Observe that dp[i][j] = dp[i - 1][j] + dp[i][j - 1].

# Note: Below is a recursive solution, but it gives time limit exceeded for large inputs:
#def uniquePaths(m, n):
#    if m == 1 and n == 1:
#        return 1
#    if m < 1 or n < 1:
#        return 0
#    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
