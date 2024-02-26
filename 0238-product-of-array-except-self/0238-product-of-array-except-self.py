class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, result, suffixProd = 1, [nums[-1]], nums[-1]
        for ind in range(len(nums) - 2, -1, -1):
            suffixProd *= nums[ind]
            result = [suffixProd] + result
        for ind in range(len(nums) - 1):
            result[ind] = prod * result[ind + 1]
            prod *= nums[ind]
        result[-1] = prod
        return result