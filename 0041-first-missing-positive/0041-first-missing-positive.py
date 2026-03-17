class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (high := max(nums)) <= 0:
            return 1
        
        has_one = False
        for ind, num in enumerate(nums):
            has_one = has_one or num == 1
            if num <= 0 or num > len(nums):
                nums[ind] = 1

        if not has_one:
            return 1

        for num in nums:
            if nums[abs(num) - 1] >= 1:
                nums[abs(num) - 1] *= -1

        for ind, num in enumerate(nums):
            if num > 0:
                return ind + 1

        return len(nums) + 1