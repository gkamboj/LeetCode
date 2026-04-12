class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.helper(candidates, 0, target, [], result)
        return result

    def helper(self, candidates, start, target, combo, result):
        if not target:
            result.append(list(combo))
            return

        for ind in range(start, len(candidates)):
            if (candidate := candidates[ind]) > target:
                break
            if ind > start and candidate == candidates[ind - 1]:
                continue
            combo.append(candidate)
            self.helper(candidates, ind + 1, target - candidate, combo, result)
            combo.pop()

'''
Approach: Backtracking (DFS)
- Sort the array first to handle duplicates and enable pruning.
- Use DFS with (start index, remaining target, current path).
- At each level, try picking elements from 'start' to end.
- If candidate > target, break (since array is sorted).
- Skip duplicates at the same recursion level:
  if i > start and nums[i] == nums[i-1]: continue
- Move forward with i + 1 (each element used at most once).
- When target == 0, add a copy of path to result.

- Time: O(2^n) worst case
- Space: O(n) recursion depth (excluding output)
'''
