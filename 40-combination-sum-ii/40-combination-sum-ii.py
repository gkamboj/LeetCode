class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(sorted(candidates), target, [], result)
        return result
    
    def solve(self, nums, target, comb, result):
        if target == 0:
            result.append(comb)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.solve(nums[i + 1:], target - nums[i], comb + [nums[i]], result)