class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        arr = [0 for i in range(len(obstacleGrid[0]))]
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                    arr[col] = 1
                elif obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    arr[col] = 0        
                elif row == 0:
                    dp[row][col] = dp[row][col - 1]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]
        
                    
# Approach: This is DP approach, similar to DP submission of LC-62, with the change being setting the position to 0 if it's blocked. To avoid extra space, input grid array is being modified.

# Below is recusrion approach with memoization (giving TLE):
#def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#    if obstacleGrid[0][0] == 1:
#        return 0
#    dp = [[-1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
#    dp[0][0] = 1
#    return self.solve(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, obstacleGrid, dp)

#def solve(self, i, j, grid, dp):
#    if i == 0 and j == 0:
#        return dp[i][j]
#    elif i < 0 or j < 0 or grid[i][j] == 1:
#        return 0
#    if dp[i - 1][j] != -1:
#        up = dp[i - 1][j]
#    else:
#        up = self.solve(i - 1, j, grid, dp)
#    if dp[i][j - 1] != -1:
#        left = dp[i][j - 1]
#    else:
#        left = self.solve(i, j - 1, grid, dp)
#    return up + left

# TC of above approach: O(n * m), Space: O(m - 1 + n - 1) + O(m * n)
#                                         recursion stack    DP size