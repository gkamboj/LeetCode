class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row_ind in range(9):
            for col_ind in range(9):
                val = board[row_ind][col_ind]
                if val != ".":
                    row_formatted_val, col_formatted_val, subsq_formatted_val = 'r' + str(row_ind) + val, 'c' + str(col_ind) + val, 's' + str(row_ind//3) + str(col_ind//3) + val
                    if row_formatted_val in seen or col_formatted_val in seen or subsq_formatted_val in seen:
                        print("seen - ", seen, "val - ", val)
                        return False
                    else:
                        seen.update([row_formatted_val, col_formatted_val, subsq_formatted_val])
        return True
        
 
