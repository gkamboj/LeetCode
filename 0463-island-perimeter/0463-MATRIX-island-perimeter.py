class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    if not row or not grid[row - 1][col]: ans += 1
                    if not col or not grid[row][col - 1]: ans += 1
                    if row == len(grid) - 1 or not grid[row + 1][col]: ans += 1
                    if col == len(grid[0]) - 1 or not grid[row][col + 1]: ans += 1
        return ans
    
'''
Approach: For every cell, check all vertices and add eligible parameter to answer.
'''    
