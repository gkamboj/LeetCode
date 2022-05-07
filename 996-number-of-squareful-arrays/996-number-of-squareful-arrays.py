class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = [0]
        self.numSquarefulRecursive(sorted(nums), [], count)
        return count[0]
    
    def numSquarefulRecursive(self, nums, perm, count):
        if not nums:
            count[0] += 1
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if perm and not self.isPerfectSquare(perm[-1] + nums[i]):
                continue
            self.numSquarefulRecursive(nums[:i] + nums[i + 1:], perm + [nums[i]], count)
        
    def isPerfectSquare(self, num):
        return int(num ** 0.5) ** 2 == num