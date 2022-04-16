class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        ans = 1
        for i in range(max(m, n), m + n -1):
            ans *= i
            ans //= (i - max(m, n) + 1)
        return int(ans)