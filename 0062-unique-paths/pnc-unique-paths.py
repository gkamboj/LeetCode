class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans, low, curr = 1, m if m < n else n, 1
        nmtr = m + n - low #nmtr = (m + n - 2) - (low - 1) + 1 
        while curr < low:
            ans = ans * nmtr // curr
            nmtr += 1
            curr += 1
        return ans
        
# Approach: Problem is to find number of ways of taking (n - 1) horizontal or (m - 1) vertical steps out of (m + n - 2) total steps that is (m + n - 2)C(m - 1). As m and n can be really large, directly applying factorial formula may result in values out of integer range. So, solve nCr = [(n - r + 1).(n - r + 2)....(n - 2).(n - 1).n] / [1.2.3....(r - 1).r]

# Note-1: To make sure that perfect division occur instead of floating answers, we have started the calculation from lowest numerator. For. eg., 6C3 = (4 / 1) * (5 / 2) * (6 / 3) is being done instead of 6C3 = (6 / 3) * (5 / 2) * (4 / 1)

# Note-2: In line 6, use ans = ans * (whatever) instead of ans *= whatever to avoid floating error.
