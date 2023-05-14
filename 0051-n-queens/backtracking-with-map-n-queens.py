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
    
# Approach: This is backtracking approach along with the use of hashing. Start by placing queen in first row and check for every combination that is every column for the given row. Whenever any combination satisfies requirement, add it to result. Remember to reset cell to '.' from 'Q' after recursive call because we need to check for every subsequent possibilities also (since every possibl combination is required).

# Note: To check if current position is valid position for the queen, hashing is used. Three types of keys are being hashed:
# 1. column containing Q with key being 'c' +. str(col). Eg., c0, c1, etc
# 2. Diagonally top right check (that is North-East direction): Observe that value (row + col) will always remain constant for this diagonal. So, hashing 'r' + str(row + col)
# 3. Digonally top left check (that is North-West direction): Observe that value (row + (n - col - 1)) will always remaind constant along the diagona;. So, hashing 'l' + str(row + n - col - 1)

# Reference: https://www.youtube.com/watch?v=i05Ju7AftcM
            
