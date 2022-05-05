class Solution:
    def grayCode(self, n: int) -> List[int]:
        start, result = 1, [0]
        while start <= n:
            result += [i + (1 << (start - 1)) for i in reversed(result)]
            start += 1
        return result
    
# Approach: This is an iterative approach.