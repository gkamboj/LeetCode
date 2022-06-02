class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, [], result)
        return result
        
    def solve(self, nums, subset, result):
        result.append(subset)
        for i in range(len(nums)):
            self.solve(nums[i + 1:], subset + [nums[i]], result)