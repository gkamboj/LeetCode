class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rowInd in range(len(board)):
            for colInd in range(len(board[rowInd])):
                if not self.isValidCell(board, rowInd, colInd):
                    return False
        return True
    
    def isValidCell(self, board, rowInd, colInd):
        if board[rowInd][colInd] == ".":
            return True
        
        val = board[rowInd][colInd]
        
        for ind in range(len(board[rowInd])):
            if ind != colInd and board[rowInd][ind] == val:
                return False
            if ind != rowInd and board[ind][colInd] == val:
                return False
            
        for boxRowInd in range(3 * (rowInd//3), 3 * (rowInd//3) + 3):
            for boxColInd in range(3 * (colInd//3), 3 * (colInd//3) + 3):
                if boxRowInd != rowInd and boxColInd != colInd and board[boxRowInd][boxColInd] == val:
                    return False
        
        return True
        
