class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.helper(candidates, [], 0, target, result)
        return result

    def helper(self, candidates, combo, start, target, result):
        if not target:
            result.append(combo[:])
            return
        
        for ind in range(start, len(candidates)):
            if (candidate := candidates[ind]) > target:
                break
            combo.append(candidate)
            self.helper(candidates, combo, ind, target - candidate, result)
            combo.pop()

        