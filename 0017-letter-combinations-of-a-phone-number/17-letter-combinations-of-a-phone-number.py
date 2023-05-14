class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d, curr, result = {}, ord('a'), []
        for i in range(2, 10):
            if i == 7 or i == 9:
                d[str(i)] = [chr(c) for c in range(curr, curr + 4)]
                curr += 4
            else:
                d[str(i)] = [chr(c) for c in range(curr, curr + 3)]
                curr += 3
        self.solve(digits, 0, '', result, d)
        return result
        
    def solve(self, digits, ind, comb, result, d):
        if ind == len(digits):
            result.append(comb)
            return
        
        for c in d[digits[ind]]:
            self.solve(digits, ind + 1, comb + c, result, d)