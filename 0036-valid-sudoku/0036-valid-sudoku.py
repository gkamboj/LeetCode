class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r_ind, row in enumerate(board):
            for c_ind, val in enumerate(row):
                if val != '.' and not self.isValidCell(r_ind, c_ind, board):
                    return False
        return True

    def isValidCell(self, x, y, board):
        cell_val = board[x][y]
        for ind, val in enumerate(board[x]):
            if ind != y and val == cell_val:
                print('hi1')
                return False

        for ind, row in enumerate(board):
            if ind != x and row[y] == cell_val:
                print('hi2')
                return False

        cell_row, cell_col = 3 * (x//3), 3 * (y//3)
        for x1 in range(cell_row, cell_row + 3):
            for y1 in range(cell_col, cell_col + 3):
                if x1 != x and y1 != y and board[x1][y1] == cell_val:
                    print('hi3')
                    return False

        return True
