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
            
# Approach: This is recursive DFS approach similar to LC-39 (Combination Sum) & LC-40 (Combination Sum 2) submissions. Refer https://leetcode.com/problems/combinations/discuss/26990/Python-easy-to-understand-DFS-solution for detail.