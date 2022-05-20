class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, perm, result):
        if not nums:
            result.append(perm)
            
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], perm + [nums[i]], result)