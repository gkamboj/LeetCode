class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.solve('', result, 0, 0, n)
        return result
    
    def solve(self, comb, result, opened, closed, n):
        if len(comb) == 2 * n:
            result.append(comb)
            return
        
        if opened < n:
            self.solve(comb + '(', result, opened + 1, closed, n)
        if closed < opened:
            self.solve(comb + ')', result, opened, closed + 1, n)