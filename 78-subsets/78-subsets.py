class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        result = []
        
        num = nums.pop(-1)
        sets = self.subsets(nums)
        result += [subset[:] for subset in sets]
        result += [subset + [num] for subset in sets]
        
        return result
    
# Approach: This is recursive approach. Find the subsets of remaining array after popping out an element num. Now, append these subsets to result and then for every subset of updated result, append another subset by including num. For baae condition, return [[], [num[0]]] when len(nums) == 1 (because for set of size 1, subsets are empty set and the given set)

# Note-1: Observe that unlike permutations problem, no for loop is used here. This is because we need to consider any element only once and not add it back after consideration.

# Note-2: Result will not be in sorted or lexicographic order.