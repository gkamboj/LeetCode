class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, rows, cols = 0, len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            area = 1

            for i, j in directions:
                if 0 <= row + i < rows and 0 <= col + j < cols and grid[row + i][col + j] == 1:
                    grid[row + i][col + j] = -1
                    area += dfs(row + i, col + j)
            
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    ans = max(ans, dfs(i, j))
                    
        return ans

'''
Approach: Recursive DFS
- Traverse the grid; when a land cell (1) is found, start DFS to explore that island.
- DFS recursively visits all 4-directionally connected land cells and returns the total area of that component.
- Mark each cell as visited (e.g., set to 0/-1) as soon as it’s processed to avoid revisits.
- Track the maximum area across all DFS calls.

Space Complexity: O(m × n) 
- Time: O(m × n), Space: O(m × n) [recursion stack in worst case]
'''
