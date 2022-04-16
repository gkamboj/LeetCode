class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        ans = 1
        for i in range(max(m, n), m + n -1):
            ans *= i
            ans //= (i - max(m, n) + 1)
        return int(ans)
    
# Approach: Problem is to find number of ways of taking (n - 1) horizontal or (m - 1) vertical steps out of (m + n - 2) total steps that is (m + n - 2)C(m - 1). As m and n can be really large, directly applying factorial formula may result in values out of integer range. So, solve nCr = [(n - r + 1).(n - r + 2)....(n - 2).(n - 1).n] / [1.2.3....(r - 1).r]