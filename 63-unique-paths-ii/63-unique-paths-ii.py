class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        arr = [0 for i in range(len(obstacleGrid[0]))]
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == 0 and col == 0:
                    arr[col] = 1
                elif obstacleGrid[row][col] == 1:
                    arr[col] = 0        
                elif row == 0:
                    arr[col] = arr[col - 1]
                elif col == 0:
                    continue
                else:
                    arr[col] += arr[col - 1]
        return arr[-1]
        
                    
# Approach: This is DP tabulation approach, similar to other DP submission but with optimised space. Here instead of 2D DP array, 1D array is being used. This is because at anytime, we just need the left and top value. Left value can be taken from arr[i - 1] index where i represent the current index, whereas top value is just the current valu that is arr[i] (as this represents ith column value from previous row).


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