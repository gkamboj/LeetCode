class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = [0]
        self.solve(sorted(nums), [], count)
        return count[0]
        
    def solve(self, nums, perm, count):
        if not nums:
            count[0] += 1
            return
        
        for i in range(len(nums)):
            if (not perm or self.isSquare(perm[-1] + nums[i])) and (i == 0 or nums[i] != nums[i - 1]):
                self.solve(nums[:i] + nums[i + 1:], perm + [nums[i]], count)
        
    def isSquare(self, n):
        return int(n ** 0.5) ** 2 == n