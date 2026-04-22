class Solution:
    def rob(self, nums: List[int]) -> int:
        v1 = v2 = 0 # v1 = dp[i-2], v2 = dp[i-1] for current i

        for num in nums:
            curr = max(num + v1, v2)
            v1 = v2
            v2 = curr
        
        return v2

'''
Approach: DP
- Define dp[i] = max money you can rob up to index i.
- Transition: dp[i] = max(dp[i-1], nums[i] + dp[i-2]) (skip vs take).
- Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1]).
- Optimize space by keeping only two variables (v1, v2) instead of full DP array.
'''
