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
            nums[ind], nums[i] = nums[i], nums[ind]
            self.solve(nums, ind + 1, result)
            nums[ind], nums[i] = nums[i], nums[ind]
            
            
# Approach: For every number, find permutations starting with that number, Repeat recursively for every position. Refer https://youtu.be/f2ic2Rsc9pU for detail.
