class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0 for i in range(len(nums))]
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        curr = nums[0]
        nums[0] = suffix[1]
        for i in range(1, len(nums) - 1):
            val = nums[i]
            nums[i] = curr * suffix[i + 1]
            curr *= val
        nums[-1] = curr
        return nums