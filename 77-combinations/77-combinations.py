class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, arr = [], [(i + 1) for i in range(n)]
        self.solve(arr, [], k, result)
        return result
    
    def solve(self, arr, comb, k, result):
        if len(comb) == k:
            result.append(comb)
            return
        
        for i in range(len(arr)):
            self.solve(arr[i + 1:], comb + [arr[i]], k, result)