class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper('', n, n, result)
        return result

    def helper(self, combo, opn, close, result):
        if not close:
            result.append(combo)
            return
        
        if opn > 0:
            self.helper(combo + '(', opn - 1, close, result)
        if close > opn:
            self.helper(combo + ')', opn, close - 1, result)

'''
Approach: Backtracking
- Use backtracking with two counters: open and close remaining.
- Add '(' if open > 0, add ')' if close > open (to keep it valid).
- When both become 0 → add the built string to the result.
'''
