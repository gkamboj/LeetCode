class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not self.isValid(board, i, j):
                    return False
        return True
            
        
        
    def isValid(self, board, rowInd, colInd):
        if board[rowInd][colInd] == '.':
            return True
        
        for i in range(len(board)):
            if i != rowInd and board[rowInd][colInd] == board[i][colInd]:
                return False
            
        for i in range(len(board[0])):
            if i != colInd and board[rowInd][colInd] == board[rowInd][i]:
                return False
            
        for i in range(rowInd//3 * 3, rowInd//3 * 3 + 3):
            for j in range(colInd//3 * 3, colInd//3 * 3 + 3):
                if (i != rowInd or j != colInd) and board[rowInd][colInd] == board[i][j]:
                    return False
                
        return True
    
# Approach: This is iterative approach. For every matrix value, check if it's valid. To check validity, 4 checks are needed: value ('.' or not), repetition in row, repetition in column and repetition in sub-square.

# Reference: https://leetcode.com/problems/valid-sudoku/discuss/15666/An-easy-to-understand-Python-solution