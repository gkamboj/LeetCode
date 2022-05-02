class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRecursive(0, candidates, target, [], result)
        return result
    
    def combinationSumRecursive(self, ind, arr, target, combination, result):
        if target == 0:
            result.append(combination)
            
        for i in range(ind, len(arr)):
            if arr[i] > target:
                continue
            self.combinationSumRecursive(ind, arr[i:], target - arr[i], combination + [arr[i]], result)
            
# Approach: This is recursive approach using DFS similar to DFS submissions of LC-78 & LC-90. To further reduce the time (in comparison to reference), check is added to ignore the iteration if element is greater than target (as combination is not possible in such case). Instead of continue, break should be used if input array is sorted.

# Reference: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.