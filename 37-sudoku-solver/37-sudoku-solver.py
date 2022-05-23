from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    self.updateVals(i, j, board, board[i][j], d, True, board[i][j])
        self.solve(board, d)
        
    
    def solve(self, board, d):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.isValid(i, j, d, str(c)):
                            self.updateVals(i, j, board, str(c), d, True, str(c))
                            if self.solve(board, d):
                                return True
                            self.updateVals(i, j, board, str(c), d, False, '.')
                    return False
        return True
                        
                        
    def isValid(self, row, col, d, val):
        if d[str(row) + 'r' + val] or d[str(col) + 'c' + val] or d[str(row // 3 * 3) + '-' + val + '-' + str(col//3 * 3)]:
            return False
        return True
        
    
    
    def updateVals(self, row, col, board, val, d, toSet, newVal):
        toSetVal = int(toSet)
        d[str(row) + 'r' + val], d[str(col) + 'c' + val], d[str(row // 3 * 3) + '-' + val + '-' + str(col//3 * 3)] = toSetVal, toSetVal, toSetVal
        board[row][col] = newVal