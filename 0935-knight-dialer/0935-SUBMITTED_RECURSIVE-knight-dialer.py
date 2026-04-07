class Solution:
    def knightDialer(self, n: int) -> int:
        possible_moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        ans, cache = 0, {}
        for num in range(10):
            ans = (ans + self.helper(possible_moves, n - 1, num, cache)) % (10 ** 9 + 7)
        
        return ans

    def helper(self, possible_moves, n, curr, cache):
        if not n:
            return 1
        
        ans = 0
        if (curr, n) in cache:
            return cache[(curr, n)]
        for move in possible_moves[curr]:
            ans += self.helper(possible_moves, n - 1, move, cache)
        cache[(curr, n)] = ans

        return ans

'''
Approach: Recursive DFS (top-down DP). FOr each digit, explore all valid moves recursively.
Use memoization to avoid recomputation and TLE.
'''
