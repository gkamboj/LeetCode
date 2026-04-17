class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False

    def helper(self, board, i, j, word):
        if not word:
            return True
        elif (
            not (0 <= i < len(board) and 0 <= j < len(board[0])) or 
            board[i][j] == '.' or 
            board[i][j] != word[0]
        ):
            return False

        orig, board[i][j] = board[i][j], '.'
        ans = (
            self.helper(board, i - 1, j, word[1:]) or
            self.helper(board, i + 1, j, word[1:]) or
            self.helper(board, i, j - 1, word[1:]) or
            self.helper(board, i, j + 1, word[1:])
        )
        board[i][j] = orig
        
        return ans
