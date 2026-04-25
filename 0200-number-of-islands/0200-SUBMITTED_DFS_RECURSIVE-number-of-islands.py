class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, row, col):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for i, j in directions:
                if 0 <= (row + i) < len(grid) and 0 <= (col + j) < len(grid[0]) and grid[row + i][col + j] == '1':
                    grid[row + i][col + j] = '-1'
                    dfs(grid, row + i, col + j)

        ans = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    ans += 1
                    grid[row][col] = '-1'
                    dfs(grid, row, col)    
                
        return ans

'''
Approach: Recursive DFS
- Traverse the grid using nested loops; whenever a land cell ('1') is found, increment count and start DFS.
- Explore all 4-directionally adjacent cells, but only if they are within bounds and equal to '1'.
- Mark each visited land cell immediately (change to '0' or '-1') to avoid revisiting.
- Each DFS call fully explores one island (connected component).

- Time: O(m × n), Space: O(m × n) (recursio stack in worst case).
'''
