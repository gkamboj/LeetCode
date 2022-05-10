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
        for c in board[i]:
            if c == 'Q':
                return False
        
        for c in range(n):
            if board[c][j] == 'Q':
                return False
        
        x, y = i, j
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            if board[x][y] == 'Q':
                return False
        
        x, y = i, j
        while x < (n - 1) and y < (n - 1):
            x += 1
            y += 1
            if board[x][y] == 'Q':
                return False
        
        x, y = i, j
        while x > 0 and y < (n - 1):
            x -= 1
            y += 1
            if board[x][y] == 'Q':
                return False
            
        x, y = i, j
        while x < (n - 1) and y > 0:
            x += 1
            y -= 1
            if board[x][y] == 'Q':
                return False
        
        return True
    
# Approach: This is backtracking approach. Start from first row and check every combination. Whenever any combination satisfies requirement, add it to result. Remember to reset cell to '.' from 'Q' after recursive call because we need to check for every subsequent possibilities also (since every possibl combination is required)

# Reference: https://www.youtube.com/watch?v=i05Ju7AftcM
            