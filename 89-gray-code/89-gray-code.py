class Solution:
    def grayCode(self, n: int) -> List[int]:
        start, result = 1, [0]
        while start <= n:
            result += [i + 2 ** (start - 1) for i in reversed(result)]
            start += 1
        return result