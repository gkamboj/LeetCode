class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.helper(candidates, [], 0, target, result)
        return result

    def helper(self, candidates, combo, start, target, result):
        if not target:
            result.append(combo[:]) # use `combo[:]` or `list(combo)`, and not `combo` as `combo` is a pointer to a list which is becoming empty at the end. Using it directly will add an empty list only.
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
- At each step, try all candidates from start onward as element reuse is allowed.
- If candidate > target, break early (because the array is sorted).
- When target == 0, add a copy of the current combo to the result.
'''
