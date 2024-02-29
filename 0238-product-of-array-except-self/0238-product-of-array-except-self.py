class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, result, suffixProd = 1, [], [nums[-1]]
        for ind in range(len(nums) - 2, -1, -1):
            suffixProd.append(suffixProd[-1] * nums[ind])
        for ind in range(len(nums) - 1):
            result.append(prod * suffixProd[len(nums) - ind - 2])
            prod *= nums[ind]
        result.append(prod)
        return result
