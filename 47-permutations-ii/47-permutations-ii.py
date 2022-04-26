from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        result, covered = [], defaultdict(int)
        
        for i in range(len(nums)):
            num = nums.pop(0)
            if covered[num] != 1:
                perms = self.permuteUnique(nums)
                for perm in perms:
                    perm.append(num)
                covered[num] = 1
                result += perms
            nums.append(num)
        
        return result
                
                    
        
# Approach: This is recursive approach (similar to LC 46 - Permutations): for every number, find permutations of remaining array and append that number at the end of these permutations. For handling duplicates, map is created to store all numbers which have been checked.

# Note: In this approach, a new map is being created for every recursive call which is using a lot of memory. So, prefer other recursive submission which is handling duplicates without using any extra memory.