class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        result = []
        
        while len(nums) > 0:
            num = nums.pop(0)
            sets = self.subsets(nums)
            result += [subset[:] for subset in sets]
            result += [subset + [num] for subset in sets]
        
        return result