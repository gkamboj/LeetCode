class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = []
        for row in board:
            for val in row:
                if val != '.':
                    arr.append(int(val))
            if not self.isValid(sorted(arr), False):
                return False
            arr = []
            
        for i in range(len(board[0])):
            for row in board:
                if row[i] != '.':
                    arr.append(int(row[i]))
            if not self.isValid(sorted(arr), True):
                return False
            arr = []
            
        for rowInd in range(0, len(board), 3):
            for colInd in range(0, len(board[0]), 3):
                for row in range(rowInd, rowInd + 3):
                    for col in range(colInd, colInd + 3):
                        if board[row][col] != '.':
                            arr.append(int(board[row][col]))
                if not self.isValid(sorted(arr), False):
                    return False
                arr = []
                
        return True
            
        
        
    def isValid(self, arr, toPrint):
        if toPrint:
            print(arr)
        isValid = True
        if len(arr) > 1:
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1]:
                    isValid = False
                    break
        return isValid