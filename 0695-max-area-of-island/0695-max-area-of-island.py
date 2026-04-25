class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, rows, cols = 0, len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 1
                    queue = deque([(i, j)])
                    grid[i][j] = -1

                    while queue:
                        row, col = queue.popleft()
                        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                        for k, l in directions:
                            if 0 <= row + k < rows and 0 <= col + l < cols and grid[row + k][col + l] == 1:
                                grid[row + k][col + l] = -1
                                area += 1
                                queue.append((row + k, col + l))
                    
                    ans = max(ans, area)

        return ans