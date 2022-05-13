class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d, curr, result = {}, ord('a'), ['']
        for i in range(2, 10):
            if i == 7 or i == 9:
                d[str(i)] = [chr(c) for c in range(curr, curr + 4)]
                curr += 4
            else:
                d[str(i)] = [chr(c) for c in range(curr, curr + 3)]
                curr += 3
        for c in digits:
            temp = []
            for r in result:
                temp += [r + char for char in d[c]]
            result = temp
        return result
        