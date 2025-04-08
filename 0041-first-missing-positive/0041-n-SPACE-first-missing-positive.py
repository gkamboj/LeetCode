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

# Approach: O(n) time with O(n) space.
# (1) Check for cases when all numbers are negative or smallest non positive != 1. Return 1 for these cases.
# (2) For remaining cases, create a helper array such that values at indexes present in original array are 1, else zero.
# Return first non-zero index.
# Return len(nums) + 1 if all values in helper are 1 (to handle cases when input is of all numbers from 1 to n)
