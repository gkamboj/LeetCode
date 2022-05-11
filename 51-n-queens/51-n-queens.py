class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        result = []
        self.solve(0, board, result)
        return result
        
    def solve(self, row, board, result):
        if row == len(board):
            result.append([''.join(val) for val in board])
            return
        
        for col in range(len(board[0])):
            if self.isValid(row, col, board, len(board)):
                board[row][col] = 'Q'
                self.solve(row + 1, board, result)
                board[row][col] = '.'
        
    
    def isValid(self, i, j, board, n):
        for c in range(i):
            if board[c][j] == 'Q':
                return False
        
        x, y = i, j
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            if board[x][y] == 'Q':
                return False
        
        x, y = i, j
        while x > 0 and y < (n - 1):
            x -= 1
            y += 1
            if board[x][y] == 'Q':
                return False
        
        return True
    
# Approach: This is backtracking approach. Start by placing queen in first row and check for every combination that is every column for the given row. Whenever any combination satisfies requirement, add it to result. Remember to reset cell to '.' from 'Q' after recursive call because we need to check for every subsequent possibilities also (since every possibl combination is required).

# Note: In isValid() method, we only need to check the area above the current position (that is diaganoally North-West, diagonally North-East and the rows of current column till the current row) and not the whole aread because for at given row, only the area above it'd be covered updto that instant.

# Reference: https://www.youtube.com/watch?v=i05Ju7AftcM
            