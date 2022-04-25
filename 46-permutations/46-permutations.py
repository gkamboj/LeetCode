class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for ind in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
            nums.append(num)
            result += perms
        
        return result