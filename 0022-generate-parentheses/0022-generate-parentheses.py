class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper('', n, n, result)
        return result

    def helper(self, combo, opn, close, result):
        if not close:
            result.append(combo)
            return
        elif not opn:
            self.helper(combo + ')', opn, close - 1, result)
        elif opn == close:
            self.helper(combo + '(', opn - 1, close, result)
        else:
            self.helper(combo + ')', opn, close - 1, result)
            self.helper(combo + '(', opn - 1, close, result)