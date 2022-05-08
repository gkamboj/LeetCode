from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occured = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != '.':
                    rowVal = str(i) + 'r-' + val
                    colVal = val + '-c' + str(j)
                    subSqVal = str(i // 3 * 3) + '-' + val + '-' + str(j // 3 * 3)
                    if occured[rowVal] or occured[colVal] or occured[subSqVal]:
                        return False
                    occured[rowVal] = 1
                    occured[colVal] = 1
                    occured[subSqVal] = 1
        return True
        
        
