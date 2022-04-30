class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.subsetsRecursively(nums, 0, result)
        return result
    
    def subsetsRecursively(self, nums, offset, result):
        if offset == len(nums) - 1:
            result.append([nums[offset]])
            return
        
        num = nums[offset]
        self.subsetsRecursively(nums, offset + 1, result)
        result += [subset + [num] for subset in result]
    
# Approach: This is recursive approach similar to other submitted recursive solutions. This approach differs in the way result variable is handled: instead of creating new result variable for every recursive call, same variable is being passed and updated in every call.