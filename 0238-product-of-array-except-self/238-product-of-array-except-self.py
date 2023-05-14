class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        result = [1]
        for ind in range(1, len(nums)):
            result.append(result[-1]*nums[ind - 1])
        right = 1
        for ind in range(len(nums) - 1, -1, -1):
            result[ind] *= right
            right *= nums[ind]
        return result
            