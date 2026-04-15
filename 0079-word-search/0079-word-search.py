class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, {}, i, j, word):
                    return True
        return False

    def helper(self, board, covered, i, j, word):
        if not word:
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False

        if (i, j) in covered:
            return False

        if board[i][j] != word[0]:
            return False

        covered[(i, j)] = 1
        word = word[1:]

        v1 = self.helper(board, covered, i + 1, j, word)
        v2 = self.helper(board, covered, i - 1, j, word)
        v3 = self.helper(board, covered, i, j + 1, word)
        v4 = self.helper(board, covered, i, j - 1, word)

        covered.pop((i, j)) 

        return v1 or v2 or v3 or v4

'''
Approach: 
'''