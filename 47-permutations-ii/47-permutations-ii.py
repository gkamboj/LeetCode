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
                    
        