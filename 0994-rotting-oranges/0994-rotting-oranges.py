class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans, m, n, levels = 0, len(grid), len(grid[0]), {0}
        queue, directions = deque(), [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    grid[row][col] = -2
                    queue.append((row, col, 0))

        
        while queue:
            i, j, level = queue.popleft()
            add = 0
            for diff_r, diff_c in directions:
                if 0 <= (r := i + diff_r) < m and 0 <= (c := j + diff_c) < n and grid[r][c] == 1:
                    grid[r][c] = -2
                    queue.append((r, c, level + 1))
                    levels.add(level + 1)
        
        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1

        return max(levels)