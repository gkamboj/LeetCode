from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        result, dictMap = [], defaultdict(int)
        self.solve(board, 0, result, dictMap)
        return result
    
    def solve(self, board, row, result, d):
        if row == len(board):
            result.append([''.join(val) for val in board])
            return
        for col in range(len(board)):
            if not d['c' + str(col)] and not d['r' + str(row + col)] and not d['l' + str(len(board) - col - 1 + row)]:
                d['c' + str(col)], d['r' + str(row + col)], d['l' + str(len(board) - col - 1 + row)] = 1, 1, 1
                board[row][col] = 'Q'
                self.solve(board, row + 1, result, d)
                board[row][col] = '.'
                d['c' + str(col)], d['r' + str(row + col)], d['l' + str(len(board) - col - 1 + row)] = 0, 0, 0