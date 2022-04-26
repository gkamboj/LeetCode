from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, covered = [], defaultdict(int)
        
        if len(nums) == 1:
            return [[nums[0]]]
        
        for ind in range(len(nums)):
            num = nums.pop(0)
            if covered[num] != 1:
                perms = self.permuteUnique(nums)
                for perm in perms:
                    perm.append(num)
                covered[num] = 1
                result += perms
            nums.append(num)
            
        return result
                    
        