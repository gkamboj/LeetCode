class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d, asciiVal = {}, 97
        for i in range(2, 10):
            if i != 7 and i != 9:
                d[str(i)] = [chr(j) for j in range(asciiVal, asciiVal + 3)]
                asciiVal += 3
            else:
                d[str(i)] = [chr(j) for j in range(asciiVal, asciiVal + 4)]
                asciiVal += 4
        
        result = []
        self.letterCombinationsRecursive(digits, d, result, 0, '')
        return result
    
    def letterCombinationsRecursive(self, digits, d, result, ind, comb):
        if len(comb) == len(digits):
            result.append(comb)
            return
        
        for i in d[digits[ind]]:
            self.letterCombinationsRecursive(digits, d, result, ind + 1, comb + i)