class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_val = max(nums)
        if min_val <= 0:
            return 1
        for val in nums:
            if val > 0 and val < min_val:
                min_val = val
        if min_val != 1:
            return 1
        helper = [0 for i in range(len(nums))]
        for val in nums:
            if val > 0 and val <= len(nums):
                helper[val - 1] = 1
        for ind, val in enumerate(helper):
            if val == 0:
                return ind + 1
        return len(nums) + 1