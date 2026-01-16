class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row_ind in range(9):
            for col_ind in range(9):
                val = board[row_ind][col_ind]
                if val == ".":
                    continue
                row_key, col_key, subsq_key = ('r', row_ind, val), ('c', col_ind, val), ('s', row_ind//3, col_ind//3, val)
                if row_key in seen or col_key in seen or subsq_key in seen:
                    return False
                else:
                    seen.update([row_key, col_key, subsq_key])
        return True
        
 
