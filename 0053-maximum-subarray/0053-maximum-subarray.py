class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = 0, -10**4 - 1
        for num in nums:
            curr += num
            ans = max(ans, curr)
            if curr < 0:
                curr = 0
        return ans
