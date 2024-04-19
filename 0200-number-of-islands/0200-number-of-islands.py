class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    ans += 1
        return ans
    
    
    def dfs(self, grid, row, col):
        if (not 0 <= row < len(grid)) or (not 0 <= col < len(grid[0])) or grid[row][col] != '1':
            return
        grid[row][col] = '#'
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)
        
'''
Approach: This is DFS approach inspired by https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
'''