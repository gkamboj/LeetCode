class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for r in range(m):
            if board[r][0] == 'O':
                self.bfs(board, r, 0)
            if board[r][n - 1] == 'O':
                self.bfs(board, r, n - 1)

        for c in range(n):
            if board[0][c] == 'O':
                self.bfs(board, 0, c)
            if board[m - 1][c] == 'O':
                self.bfs(board, m - 1, c)
                    
        
        for row in board:
            for ind, cell in enumerate(row):
                if cell == 'O':
                    row[ind] = 'X'
                elif cell == 'T':
                    row[ind] = 'O'
        

    def bfs(self, board, i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])

        queue = deque([(i, j)])
        board[i][j] = 'T'

        while queue:
            r, c = queue.popleft()
            for diff_r, diff_c in directions:
                if 0 <= (r1 := r + diff_r) < m and 0 <= (c1 := c + diff_c) < n and board[r1][c1] == 'O':
                    board[r1][c1] = 'T'
                    queue.append((r1, c1))

'''
Approach: BFS
 -Start from all boundary 'O' cells and run BFS to mark all connected 'O' as safe (e.g., mark as 'T').
- These marked cells represent regions that cannot be captured.
- Traverse the board:
- Convert remaining 'O' → 'X' (captured regions)
- Convert 'T' → 'O' (restore safe regions)

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)
'''