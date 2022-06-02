class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(sorted(candidates), [], result, target)
        return result
    
    def solve(self, nums, comb, result, target):
        if target == 0:
            result.append(comb)
            return
        
        for i in range(len(nums)):
            if nums[i] > target:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.solve(nums[i + 1:], comb + [nums[i]], result, target - nums[i])