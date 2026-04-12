class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, queue = [], deque([([], 0, target)])
        
        while queue:
            combo, ind, target = queue.popleft()

            if not target:
                result.append(combo)
                continue

            for i in range(ind, len(candidates)):
                if (candidate := candidates[i]) > target:
                    break
                queue.append((combo + [candidate], i, target - candidate))
        
        return result
            


'''
Approach: Iterative BFS
- Use a queue to process states (combo, index, target) level by level (FIFO).
- Pop a state → try all candidates from current index onward.
- Push new states with updated combo and reduced target into the queue.
- Add to result when target becomes 0.
- Sorting helps prune: if candidate > target → break early.
- It's BFS as we process all states at current depth before moving deeper.
- The only difference from the iterative DFS approach is that here we use FIFO (queue) to explore all partial combinations level by level, whereas DFS uses 
LIFO (stack) to go deep into one combination before exploring others, making DFS more space-efficient.

- Not very efficient:
  - Queue can grow very large (stores many intermediate states).
  - Explores unnecessary breadth instead of going deep early.
  - Higher memory usage compared to DFS/backtracking due to new list created for every step (by `combo + [candidate]`).
  - Backtracking DFS is preferred as it is more space-efficient and natural for combination generation.
'''
