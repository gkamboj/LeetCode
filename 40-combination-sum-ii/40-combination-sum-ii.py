class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRecursively(sorted(candidates), target, [], result)
        return result
    
    def combinationSumRecursively(self, arr, target, subset, result):
        if target == 0:
            result.append(subset)
            return
        
        for i in range(len(arr)):
            if arr[i] > target:
                break
            if i > 0 and arr[i - 1] == arr[i]:
                continue
            self.combinationSumRecursively(arr[i + 1:], target - arr[i], subset + [arr[i]], result)