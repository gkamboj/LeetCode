class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_prod, prev = [0 for i in range(len(nums))], 1
        for ind in range(len(nums) - 1, -1, -1):
            right_prod[ind] = prev * nums[ind]
            prev = right_prod[ind]
        result, prev = [], 1
        for ind in range(len(nums) - 1):
            result.append(prev * right_prod[ind + 1])
            prev *= nums[ind]
        result.append(prev)
        return result