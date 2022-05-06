class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        self.grayCodeRecursive(n, result)
        return result
        
    def grayCodeRecursive(self, n, result):
        if n == 0:
            result.append(0)
            return
        
        self.grayCodeRecursive(n - 1, result)
        result += [i | (1 << (n - 1)) for i in reversed(result)]