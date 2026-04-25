class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, rows, cols = 0, len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 1
                    queue = deque([(i, j)])
                    grid[i][j] = -1

                    while queue:
                        row, col = queue.popleft()

                        for rdiff, cdiff in directions:
                            if 0 <= row + rdiff < rows and 0 <= col + cdiff < cols and grid[row + rdiff][col + cdiff] == 1:
                                grid[row + rdiff][col + cdiff] = -1
                                area += 1
                                queue.append((row + rdiff, col + cdiff))
                    
                    ans = max(ans, area)

        return ans

'''
Approach: BFS
- Traverse the grid; for each land cell, run BFS to explore the entire island.
- Count the number of cells visited during BFS as the area.
- Track maximum area across all islands.

- Time: O(m × n), Space: O(m × n)
'''
