class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, stack = [], [('', n, n)]
        
        while stack:
            combo, opn, close = stack.pop()

            if not close:
                result.append(combo)
                continue
            
            if close > opn:
                stack.append((combo + ')', opn, close - 1))

            if opn > 0:
                stack.append((combo + '(', opn - 1, close))
            
        return result


'''
Approach: Iterative DFS
- Use a stack to simulate recursion (LIFO).
- Pop a state → expand it → push next states.
- Go deep along one path first, then backtrack.
- It's DFS as we are following LIFO, that is, going as deep as possible down one branch before trying others.
- The only difference from the iterative BFS submission is that we use FIFO there (using a queue) to process a level before going further in depth.
'''
