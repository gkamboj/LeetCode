class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True
        return False

    def helper(self, board, i, j, word, ind):
        if ind == len(word):
            return True
        elif (
            not (0 <= i < len(board) and 0 <= j < len(board[0])) or 
            board[i][j] != word[ind]
        ):
            return False

        orig, board[i][j] = board[i][j], '.'
        ans = (
            self.helper(board, i - 1, j, word, ind + 1) or # use ind instead of word[1:] to prevent slicing everytime
            self.helper(board, i + 1, j, word, ind + 1) or
            self.helper(board, i, j - 1, word, ind + 1) or
            self.helper(board, i, j + 1, word, ind + 1)
        )
        board[i][j] = orig
        
        return ans

'''
Approach: Backtracking + DFS
- For every cell, explore 4 directions, and mark visited in-place and restore after recursion.
- Track progress with index parameter (ind)
- Optionals that could be added to solution:
    - Prune early: if board character counts can’t cover the word, return False immediately.
    - Reverse the word to start from the rarer character if if frequence of first character is higher → reduces branching.
'''