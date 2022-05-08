class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occured = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != '.':
                    rowVal = str(i) + 'r-' + val
                    colVal = val + '-c' + str(j)
                    subSqVal = str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
                    if rowVal in occured or colVal in occured or subSqVal in occured:
                        return False
                    occured.append(rowVal)
                    occured.append(colVal)
                    occured.append(subSqVal)
        return True
        
        
