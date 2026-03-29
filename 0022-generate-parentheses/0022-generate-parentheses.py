class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(result, n, n, '')
        return result

    def helper(self, result, start, end, val):
        if not end:
            result.append(val)
        elif not start:
            self.helper(result, start, end - 1, val + ')')
        else:
            self.helper(result, start - 1, end, val + '(')
            if start < end:
                self.helper(result, start, end - 1, val + ')')
