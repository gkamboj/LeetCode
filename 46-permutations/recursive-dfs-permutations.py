class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, [], result)
        return result
    
    def solve(self, nums, perm, result):
        if not nums:
            result.append(perm)
            return
        
        for i in range(len(nums)):
            self.solve(nums[:i] + nums[i + 1:], perm + [nums[i]], result)
            
# Approach: This is recursive DFS approach. 
