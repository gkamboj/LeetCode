class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, ans, curr = 0, len(nums) + 1, 0
        for end in range(len(nums)):
            curr += nums[end]
            while curr >= target:
                ans = min(ans, end - start + 1)
                curr -= nums[start]
                start += 1
        return ans if ans != len(nums) + 1 else 0
    
# Approach: This is 2-pointer approach. Keep moving end pointer till sum becomes more than target. Then, begin moving start pointer till sum becomes less than target, updating ans all along. TC: O(n) as each element can be visited at max twice: once each by start and end pointer, Space: O(1)