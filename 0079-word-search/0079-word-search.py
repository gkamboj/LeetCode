class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        def isWordPresentDFS(i, j, word):
            if not word: return True

            if not 0 <= i < len(board) or \
            not 0 <= j < len(board[0]) or \
            board[i][j] != word[0]:
                return False

            temp = board[i][j]
            board[i][j] = '#'
            result = isWordPresentDFS(i + 1, j, word[1:]) or \
            isWordPresentDFS(i, j + 1, word[1:]) or \
            isWordPresentDFS(i - 1, j, word[1:]) or \
            isWordPresentDFS(i, j - 1, word[1:])
            board[i][j] = temp
            
            return result
        
        for row_ind in range(len(board)):
            for col_ind in range(len(board[0])):
                if isWordPresentDFS(row_ind, col_ind, word):
                    return True
        return False
        
        
# Approach: DFS, refer https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.