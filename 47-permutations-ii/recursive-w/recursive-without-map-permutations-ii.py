from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.recursivePermuteUnique(nums)
    
    def recursivePermuteUnique(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        
        result, prev = [], -11
        
        for ind in range(len(nums)):
            num = nums.pop(0)
            if num != prev:
                perms = self.recursivePermuteUnique(nums)
                for perm in perms:
                    perm.append(num)
                result += perms
            prev = num
            nums.append(num)
            
        return result
                    
        
# Approach: This is recursive approach (similar to LC 46 - Permutations). For handling duplicates, sort the input before passing it to recursive method and while handling any number, check if it's not equal to its previous

# Note: New method is created instead of using the given method because we need sorted input only for the given input array, not for every recursive call. To understand this, take example of [1, 2, 2]: observe that after first iteration, we'll have [2, 2, 1] in result. During 2nd iteration, nums will be [2, 1] after the pop(0), but on calling the recusive methof it'll get changed to [1, 2] due to sorting, which is not what we want.
