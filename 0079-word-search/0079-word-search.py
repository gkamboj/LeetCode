class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, {}, word):
                    return True
        return False

    def helper(self, board, i, j, covered, word):
        if not word:
            return True
        elif (
            not (0 <= i < len(board) and 0 <= j < len(board[0])) or 
            (i, j) in covered or 
            word[0] != board[i][j]
        ):
            return False

        covered[(i, j)] = 1
        ans = (
            self.helper(board, i - 1, j, covered, word[1:]) or
            self.helper(board, i + 1, j, covered, word[1:]) or
            self.helper(board, i, j - 1, covered, word[1:]) or
            self.helper(board, i, j + 1, covered, word[1:])
        )
        del covered[(i, j)]
        
        return ans

# A B C E
# S F E S
# A D E E