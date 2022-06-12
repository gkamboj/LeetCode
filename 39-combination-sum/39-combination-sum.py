class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(candidates, result, [], 0, target)
        return result
    
    def solve(self, nums, result, comb, ind, target):
        if ind >= len(nums):
            if target == 0:
                result.append(comb)
            return
        if target < 0:
            return
        self.solve(nums, result, comb + [nums[ind]], ind, target - nums[ind])
        self.solve(nums, result, comb, ind + 1, target)