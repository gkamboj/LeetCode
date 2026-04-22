class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for i in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1]

'''
Approach: DP
- Define dp[i] = max money you can rob up to index i.
- Transition: dp[i] = max(dp[i-1], nums[i] + dp[i-2]) (skip vs take).
- Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1]).
- Optimize space by keeping only two variables (prev1, prev2) instead of full DP array.
'''