class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for ind in range(len(nums)):
            ans = ans + (ind + 1) - nums[ind]
        return ans

# Approach: Same as subtracting array sum from sum of first n numbers, but doing in loop to avoid overflow that can happen in case of high n.
