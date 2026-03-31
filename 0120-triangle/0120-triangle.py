class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]              

'''
Approach: Bottom-up DP starting from the last row and iteratively moving upwards.
At each cell, compute the minimum path sum using the two adjacent values from the row below.
'''