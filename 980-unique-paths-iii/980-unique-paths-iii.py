class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        result, count, row, col = [0], 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row, col = i, j
                count += grid[i][j] == 0
        self.solve(grid, result, count, row, col)
        return result[0]
    
    def solve(self, grid, result, count, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1:
            val = grid[i][j]
            if val == 2 and count == -1:
                result[0] += 1
                return
            grid[i][j] = -1
            self.solve(grid, result, count - 1, i - 1, j)
            self.solve(grid, result, count - 1, i + 1, j)
            self.solve(grid, result, count - 1, i, j - 1)
            self.solve(grid, result, count - 1, i, j + 1)
            grid[i][j] = val
        
        