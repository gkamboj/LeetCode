from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        result, d = [], defaultdict(int)
        self.solve(0, board, result, d)
        return result
        
    def solve(self, row, board, result, d):
        if row == len(board):
            result.append([''.join(val) for val in board])
            return
        
        for col in range(len(board[0])):
            if not d['c' + str(col)] and not d['r' + str(row + col)] and not d['l' + str(row - col - 1 + len(board))]:
                board[row][col] = 'Q'
                d['c' + str(col)], d['r' + str(row + col)], d['l' + str(row - col - 1 + len(board))] = 1, 1, 1
                self.solve(row + 1, board, result, d)
                board[row][col] = '.'
                d['c' + str(col)], d['r' + str(row + col)], d['l' + str(row - col - 1 + len(board))] = 0, 0, 0
    
# Approach: This is backtracking approach. Start by placing queen in first row and check for every combination that is every column for the given row. Whenever any combination satisfies requirement, add it to result. Remember to reset cell to '.' from 'Q' after recursive call because we need to check for every subsequent possibilities also (since every possibl combination is required).

# Note: In isValid() method, we only need to check the area above the current position (that is diaganoally North-West, diagonally North-East and the rows of current column till the current row) and not the whole aread because for at given row, only the area above it'd be covered updto that instant.

# Reference: https://www.youtube.com/watch?v=i05Ju7AftcM
            