class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(sorted(candidates), target, [], result, 0)
        return result
    
    def solve(self, nums, target, comb, result, ind):
        if target == 0:
            result.append(comb)
            return
        
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.solve(nums, target - nums[i], comb + [nums[i]], result, i + 1)