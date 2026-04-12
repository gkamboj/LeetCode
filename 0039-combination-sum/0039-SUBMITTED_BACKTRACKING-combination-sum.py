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

'''
Approach: Backtracking + DFS
- Sort the candidates to enable early pruning.
- Use DFS/backtracking with parameters: combo, start, and target.
- At each step, try all candidates from start onward as elements reuse is allowed.
- If candidate > target, break early (because array is sorted).
- When target == 0, add a copy of current combo to result.
'''
