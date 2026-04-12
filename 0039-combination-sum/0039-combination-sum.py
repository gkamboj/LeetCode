class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, stack = [], [([], 0, target)]
        
        while stack:
            combo, ind, target = stack.pop()

            if not target:
                result.append(combo)
                continue

            for i in range(ind, len(candidates)):
                if (candidate := candidates[i]) > target:
                    break
                stack.append((combo + [candidate], i, target - candidate))
        
        return result
            


'''
Approach: Iterative DFS
- Use a stack to process states (combo, index, target) in depth-first manner (LIFO).
- Pop a state → try all candidates from current index onward.
- Push new states with updated combo and reduced target into the stack.
- Add to result when target becomes 0.
- Sorting helps prune: if candidate > target → break early.
- It's DFS as we go deep into one combination before exploring others (due to LIFO order).
- The only difference from the iterative BFS approach is that here we use LIFO (stack) to go deep into one combination before processing others, whereas BFS 
uses FIFO (queue) to explore all partial combinations level by level.

- Not very efficient:
  - Still creates new lists at every step (`combo + [candidate]`).
  - More overhead compared to backtracking (no in-place modification).
  - Stack can still grow large, though usually smaller than BFS queue.
  - Recursive backtracking DFS is preferred as it is more space-efficient (uses append/pop) and avoids repeated copying.
'''