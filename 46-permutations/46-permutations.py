class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.solve(nums)
    
    
    def solve(self, nums):
        if len(nums) == 1:
            return [nums[:]]
        
        result = []
        for ind in range(len(nums)):
            num = nums.pop(0)
            perms = self.solve(nums)
            for perm in perms:
                perm.append(num)
            nums.append(num)
            result += perms
            
        return result