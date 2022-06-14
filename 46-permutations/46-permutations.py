class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, result)
        return result
    
    
    def solve(self, nums, ind, result):
        if ind == len(nums):
            result.append(nums[:])
            return
        
        for i in range(ind, len(nums)):
            nums[i], nums[ind] = nums[ind], nums[i]
            self.solve(nums, ind + 1, result)
            nums[i], nums[ind] = nums[ind], nums[i]