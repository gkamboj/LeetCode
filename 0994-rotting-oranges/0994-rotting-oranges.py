class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])
        queue, directions = deque(), [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))

        
        while queue:
            change = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for diff_r, diff_c in directions:
                    if 0 <= (r := i + diff_r) < m and 0 <= (c := j + diff_c) < n and grid[r][c] == 1:
                        queue.append((r, c))
                        grid[r][c] = 2
                        change = True
            if change:
                ans += 1

        for row in grid:
            if 1 in row:
                return -1

        return ans

'''
Approach: BFS
- Treat all rotten oranges as starting points simultaneously and add them to the queue.
- Perform level-order BFS, where each level represents 1 minute of spread.
- For each cell, rot all adjacent fresh oranges (1) and enqueue them.
- Increment time only if at least one orange rots in that level.
- After BFS, if any fresh orange remains → return -1, else return total time.

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)
'''