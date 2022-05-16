from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute(sorted(nums), [], result)
        return result
        
    def permute(self, nums, perm, result):
        if not nums:
            result.append(perm)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.permute(nums[:i] + nums[i + 1:], perm + [nums[i]], result)
            
# Approach: This is recursive DFS approach. Pass the sorted array to recursive method. For every index, if current index element is not equal to previous element then call the method again recursively by updating perm.

# Reference: https://leetcode.com/problems/permutations-ii/discuss/18649/Python-easy-to-understand-backtracking-solution