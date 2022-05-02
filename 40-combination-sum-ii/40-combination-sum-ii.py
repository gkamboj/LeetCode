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
            
# Approach: This recursive DFS approach similar LC-40, 78, 90 submissions. Note that since duplicates are not allowed, arr[i + 1:] is passed as array for next iteration.

# Time complexity: In worst case, all 2^n subsets will be checked and there is sorting also => O(2^n + n logn) = O(2^n)

# Space complexity: Recusrion stack will take O(n) in worst case