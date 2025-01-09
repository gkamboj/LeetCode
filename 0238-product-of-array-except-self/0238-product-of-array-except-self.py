class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, result, right = len(nums), [1], 1
        for ind in range(1, n):
            result.append(result[-1] * nums[ind - 1])
        for ind in range(n - 1, -1, -1):
            result[ind] *= right
            right *= nums[ind]
        return result
