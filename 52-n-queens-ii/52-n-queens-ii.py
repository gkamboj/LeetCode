class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for i in range(n)] for j in range(n)]
        count = [0]
        self.solve(0, board, count)
        return count[0]
        
    def solve(self, row, board, result):
        if row == len(board):
            result[0] += 1
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