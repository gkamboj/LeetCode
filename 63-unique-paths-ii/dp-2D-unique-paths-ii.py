class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == 0 and col == 0:
                    continue
                elif obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                elif row == 0:
                    obstacleGrid[row][col] = int(obstacleGrid[row][col - 1] == 1)
                elif col == 0:
                    obstacleGrid[row][col] = int(obstacleGrid[row - 1][col] == 1)
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[-1][-1]
                    
# Approach: This is DP approach, similar to DP submission of LC-62, with the change being setting the position to 0 if it's blocked. To avoid extra space, input grid array is being modified.
