class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(sorted(nums), result, [])
        return result
    
    def solve(self, nums, result, subset):
        result.append(subset)
        for ind in range(len(nums)):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            self.solve(nums[ind + 1:], result, subset + [nums[ind]])