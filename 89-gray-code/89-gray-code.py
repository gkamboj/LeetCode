class Solution:
    def grayCode(self, n: int) -> List[int]:
        result, curr = [0], 0
        while curr < n:
            result += [i + (1 << curr) for i in reversed(result)]
            curr += 1
        return result