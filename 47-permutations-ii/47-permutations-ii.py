from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute(sorted(nums), [], result)
        return result
        
    def permute(self, nums, perm, result):
        if not nums:
            result.append(perm)
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.permute(nums[:i] + nums[i + 1:], perm + [nums[i]], result)