class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        result = []
        
        #while len(nums) > 0:
        num = nums.pop(-1)
        sets = self.subsets(nums)
        result += [subset[:] for subset in sets]
        result += [subset + [num] for subset in sets]
        
        return result
    
# Approach: This is recursive approach. Find the subsets of remaining array after popping out an element num. Now, append these subsets to result and then for every subset of updated result, append another subset by including num. For baae condition, return [[], [num[0]]] when len(nums) == 1 (because for set of size 1, subsets are empty set and the given set)

# Note-1: Observe that insetad of for loop, while condition is used in line-8. This is because num is not appended back after popping (which was being done for permutations) and hence length of nums is decreasing.

# Note-2: