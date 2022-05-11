class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        result = [0]
        startRow, startCol, count = 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startRow, startCol = i, j
                count += (grid[i][j] == 0)
        self.solve(grid, startRow, startCol, count, result)
        return result[0]
        
    def solve(self, grid, i, j, count, result):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1:
            val = grid[i][j]
            if val == 2 and count == -1:
                result[0] += 1
            else:
                grid[i][j] = -1
                self.solve(grid, i - 1, j, count - 1, result)
                self.solve(grid, i + 1, j, count - 1, result)
                self.solve(grid, i, j + 1, count - 1, result)
                self.solve(grid, i, j - 1, count - 1, result)
                grid[i][j] = val
            
# Approach: This is backtracking approach using DFS. Call the recursive method with starting indices and keep on recursively calling the method for all 4 directions. Whenever base conditions is matched, update the result counter.

# Reference: https://leetcode.com/problems/unique-paths-iii/discuss/885019/Python-easy-to-understand-backtracking-solution