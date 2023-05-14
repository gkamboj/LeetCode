from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = defaultdict(int)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    self.update(board, d, row, col, board[row][col], True, board[row][col])
        self.solve(board, d)
        
        
    def solve(self, board, d):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == '.':
                    for c in range(1, 10):
                        if self.isValid(board, d, row, col, str(c)):
                            self.update(board, d, row, col, str(c), True, str(c))
                            if self.solve(board, d):
                                return True
                            self.update(board, d, row, col, str(c), False, '.')
                    return False
        return True
    
    
    def isValid(self, board, d, row, col, val):
        if not d[str(row) + 'r' + val] and not d[str(col) + 'c' + val] and not d[str(row // 3 * 3) + 'b' + str(col // 3 * 3) + '-' + val]:
            return True
        return False
    
    def update(self, board, d, row, col, val, toSet, newVal):
        d[str(row) + 'r' + val], d[str(col) + 'c' + val], d[str(row // 3 * 3) + 'b' + str(col // 3 * 3) + '-' + val] = int(toSet), int(toSet), int(toSet)
        board[row][col] = newVal
        
        