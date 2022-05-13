class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1 for i in range(n)]
        for row in range(1, m):
            for col in range(1, n):
                arr[col] += arr[col - 1]
        return arr[-1]