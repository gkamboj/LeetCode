class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, [], result, 0)
        return result
        
    def solve(self, nums, subset, result, ind):
        if ind >= len(nums):
            result.append(subset)
            return
        
        self.solve(nums, subset + [nums[ind]], result, ind + 1)
        self.solve(nums, subset, result, ind + 1)
        
# Approach: https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
