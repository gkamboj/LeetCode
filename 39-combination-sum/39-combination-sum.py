class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRecursive(candidates, target, [], result)
        return result
    
    def combinationSumRecursive(self, arr, target, combination, result):
        if target == 0:
            result.append(combination)
        
        if target < 0:
            return
            
        for i in range(len(arr)):
            if arr[i] > target:
                continue
            self.combinationSumRecursive(arr[i:], target - arr[i], combination + [arr[i]], result)
            