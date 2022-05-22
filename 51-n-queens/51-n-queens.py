from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        result, d = [], defaultdict(int)
        self.solve(board, result, 0, d)
        return result
    
    def solve(self, board, result, row, d):
        if row == len(board):
            result.append([''.join(val) for val in board])
            return
            
        for col in range(len(board[0])):
            if not d['c' + str(col)] and not d['r' + str(row + col)] and not d['l' +str(len(board) - col - 1 + row)]:
                d['c' + str(col)], d['r' + str(row + col)], d['l' +str(len(board) - col - 1 + row)] = 1, 1, 1
                board[row][col] = 'Q'
                self.solve(board, result, row + 1, d)
                d['c' + str(col)], d['r' + str(row + col)], d['l' +str(len(board) - col - 1 + row)] = 0, 0, 0
                board[row][col] = '.'
                
