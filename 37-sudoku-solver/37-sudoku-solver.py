from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != '.':
                    rowVal, colVal, subSqVal = str(i) + 'r-' + val, val + '-c' + str(j), str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
                    d[rowVal] = 1
                    d[colVal] = 1
                    d[subSqVal] = 1
        self.solve(board, d)
        
    def solve(self, board, d):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.isValid(board, i, j, d, str(c)):
                            board[i][j] = str(c)
                            rowVal, colVal, subSqVal = str(i) + 'r-' + str(c), str(c) + '-c' + str(j), str(i // 3 * 3) + '-' + str(c) + '-' + str(j // 3 * 3)
                            d[rowVal] = 1
                            d[colVal] = 1
                            d[subSqVal] = 1
                            if self.solve(board, d):
                                return True
                            else:
                                board[i][j] = '.'
                                d[rowVal] = 0
                                d[colVal] = 0
                                d[subSqVal] = 0
                    return False
        return True
        
        
    def isValid(self, board, i, j, d, val):
        isValid = True
        rowVal, colVal, subSqVal = str(i) + 'r-' + val, val + '-c' + str(j), str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
        if d[rowVal] or d[colVal] or d[subSqVal]:
            isValid = False
        return isValid