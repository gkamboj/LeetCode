from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.permute(sorted(nums))
        
    def permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        
        result, perv = [], -11
        
        for i in range(len(nums)):
            num = nums.pop(0)
            if num != perv:
                perms = self.permute(nums)
                for perm in perms:
                    perm.append(num)
                result += perms
            nums.append(num)
            perv = num
        
        return result