from collections import defaultdict

class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for i in range(n)] for j in range(n)]
        d, count = defaultdict(int), [0]
        return self.solve(0, board, d, count)
        
    def solve(self, row, board, d, count):
        if row == len(board):
            return 1
        ans = 0
        for col in range(len(board[0])):
            if not d['c' + str(col)] and not d['r' + str(row + col)] and not d['l' + str(row - col - 1 + len(board))]:
                board[row][col] = 'Q'
                d['c' + str(col)] = 1
                d['r' + str(row + col)] = 1
                d['l' + str(row - col - 1 + len(board))] = 1
                ans += self.solve(row + 1, board, d, count)
                board[row][col] = '.'
                d['c' + str(col)] = 0
                d['r' + str(row + col)] = 0
                d['l' + str(row - col - 1 + len(board))] = 0
        return ans
                
                
# Approach: This is backtracking approach. Refer LC-51 for explanation.
