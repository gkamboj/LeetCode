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
            
# Approach: See https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution and its comments:
# (i) https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/10980 
# (ii) https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution/128130
