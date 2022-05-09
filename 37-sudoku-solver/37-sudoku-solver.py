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
                    self.updateVals(board, d, True, val, i, j, val)
        self.solve(board, d)
        
    def solve(self, board, d):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.isValid(i, j, d, str(c)):
                            self.updateVals(board, d, True, str(c), i, j, str(c))
                            if self.solve(board, d):
                                return True
                            else:
                                self.updateVals(board, d, False, str(c), i, j, '.')
                    return False
        return True
        
        
    def isValid(self, i, j, d, val):
        isValid = True
        rowVal, colVal, subSqVal = str(i) + 'r' + val, val + 'c' + str(j), str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
        if d[rowVal] or d[colVal] or d[subSqVal]:
            isValid = False
        return isValid
    
    def updateVals(self, board, d, toSet, val, i, j, newVal):
        rowVal, colVal, subSqVal = str(i) + 'r' + val, val + 'c' + str(j), str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
        d[rowVal] = int(toSet)
        d[colVal] = int(toSet)
        d[subSqVal] = int(toSet)
        board[i][j] = newVal
        
# Approach: This is backtracking apporach. A map is being maintained to store all the values already existing, to reduce the complexity of isValid method to O(1) instead of running double for loop everytime. Also, since we need to make 3 checks (row, column and subsquare), these 3 corresponding values are stored in map for every possible cell.

# Reference: https://www.youtube.com/watch?v=FWAIf_EVUKE