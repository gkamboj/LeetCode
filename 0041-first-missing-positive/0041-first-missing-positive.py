class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_present = False
        for ind, num in enumerate(nums):
            one_present = one_present or num==1
            if num <= 0 or num > len(nums):
                nums[ind] = 1
        if not one_present: return 1
        print(nums)
        for ind, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            
        print(nums)
        for ind in range(len(nums)):
            if nums[ind] > 0:
                return ind + 1
        return len(nums) + 1