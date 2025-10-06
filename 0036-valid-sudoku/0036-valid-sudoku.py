class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = set()
        cols_seen = set()
        boxes_seen = set()
    
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val==".":
                    continue
                box_key=(r//3,c//3,val)
                row_key=(r,val)
                col_key=(c,val)
    
                if row_key in rows_seen or col_key in cols_seen or box_key in boxes_seen:
                    return False
                rows_seen.add(row_key)
                cols_seen.add(col_key)
                boxes_seen.add(box_key)
        return True

# Interview - candidate solution