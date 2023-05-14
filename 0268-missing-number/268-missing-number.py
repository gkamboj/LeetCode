class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for ind in range(len(nums)):
            ans = ans + (ind + 1) - nums[ind]
        return ans