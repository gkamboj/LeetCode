class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, queue = [], deque([('', n, n)])
        
        while queue:
            combo, opn, close = queue.popleft()

            if not close:
                result.append(combo)
                continue
            
            if opn > 0:
                queue.append((combo + '(', opn - 1, close))
            
            if close > opn:
                queue.append((combo + ')', opn, close - 1))
            
        return result


'''
Approach: Iterative BFS
- Use a queue to process states level by level (FIFO).
- Pop a state → add all its next states to the queue.
- Explore all states at the current depth before going deeper.
- Add to the result if all parentheses have been taken care of.
- It's BFS as we are following FIFO, that is, exploring all nodes at a level before adding new ones.
- The only difference from the iterative DFS submission is that we use LIFO there (using a stack) to go in depth before processing others.
'''
