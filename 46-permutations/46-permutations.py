class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        result = []
        
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            nums.append(num)
            for perm in perms:
                perm.append(num)
            result += perms
            
        return result