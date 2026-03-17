class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (high := max(nums)) <= 0:
            return 1
        
        n = min(len(nums), high) + 1
        arr = [1 for i in range(n)]
        
        for num in nums:
            if 0 < num < n:
                arr[num] = 0
        
        for ind, num in enumerate(arr):
            if ind and num:
                return ind
        
        return n

# Approach: O(n) time with O(n) space.
# (1) If all numbers are non-positive, directly return 1.
# (2) For the remaining cases, create a helper array of a length of at least the length of nums and the maximum of nums,
# with every member set as 1. For every number of nums, set the value at the corresponding index to 0.
# Return the first index with a non-zero value.
# Return len(nums) + 1 if all values in helper are 0 (to handle cases when input is of all numbers from 1 to n)
