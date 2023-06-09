class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        num, den = 1, 1
        while n > 1:
            num *= (m + n - 2)
            den *= (n - 1)
            n -= 1
        ans = num // den
        return ans