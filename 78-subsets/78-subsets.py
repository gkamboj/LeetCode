class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsetsRecursively(nums, 0)
    
    def subsetsRecursively(self, nums, offset):
        if offset == len(nums) - 1:
            return [[], [nums[offset]]]
        
        result = []
        num = nums[offset]
        sets = self.subsetsRecursively(nums, offset + 1)
        result += [subset[:] for subset in sets]
        result += [subset + [num] for subset in sets]
        return result
    
# Approach: This is recursive approach similar to other submitted recursive approach. Only difference is: instead of popping the element of array, offset is being used to track the array index. This approach can be used if modification of original input is not allowed.
