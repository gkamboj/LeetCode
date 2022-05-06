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
        result, firstDone = [], False
        for c in digits[::-1]:
            if firstDone:
                temp = []
                for comb1 in d[c]:
                    for comb2 in result:
                        temp.append(comb1 + comb2)
                result = temp
            else:
                result = d[c]
                firstDone = True
                
        return result