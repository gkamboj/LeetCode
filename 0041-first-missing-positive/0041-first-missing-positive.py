class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (high := max(nums)) <= 0:
            return 1
        n = min(len(nums), high) + 1
        arr = [1 for i in range(n)]
        
        for num in nums:
            if 0 < num < n:
                arr[num] = 0
        
        for ind, num in enumerate(arr):
            if ind and num:
                return ind
        
        return n