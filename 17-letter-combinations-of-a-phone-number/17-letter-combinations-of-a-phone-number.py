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
        
        result = [""]
        while len(result[0]) != len(digits):
            curr = result.pop(0)
            currDigit = d[str(digits[len(curr)])]
            for char in currDigit:
                result.append(curr + char)
                
        return result