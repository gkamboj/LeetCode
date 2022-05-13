class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans, low, curr = 1, m if m < n else n, 1
        nmtr = m + n - low
        while curr < low:
            ans = ans * nmtr // curr
            nmtr += 1
            curr += 1
        return ans
        