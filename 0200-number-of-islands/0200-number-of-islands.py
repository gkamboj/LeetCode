class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    ans += 1
                    
                    queue = deque([(row, col)])
                    grid[row][col] = '-1'
                    while queue:
                        i, j = queue.popleft()
                        if i + 1 < m and grid[i + 1][j] == '1':
                            queue.append((i + 1, j))
                            grid[i + 1][j] = '-1'
                        if j + 1 < n and grid[i][j + 1] == '1':
                            queue.append((i, j + 1))
                            grid[i][j + 1] = '-1'
                        if i > 0 and grid[i - 1][j] == '1':
                            queue.append((i - 1, j))
                            grid[i - 1][j] = '-1'
                        if j > 0 and grid[i][j - 1] == '1':
                            queue.append((i, j - 1))
                            grid[i][j - 1] = '-1'
        
        return ans
