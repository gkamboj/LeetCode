class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(sorted(candidates), [], target, result)
        return result
    
    def dfs(self, candidates, comb, target, result):
        if target == 0:
            result.append(comb)
            return
        
        for i in range(len(candidates)):
            if (i > 0 and candidates[i - 1] == candidates[i]) or candidates[i] > target:
                continue
            self.dfs(candidates[i + 1:], comb + [candidates[i]], target - candidates[i], result)