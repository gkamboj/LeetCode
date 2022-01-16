class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        return len(nums) * (len(nums) + 1) // 2 - total
    
#Approach: Sum first n natural number and subtract sum of array