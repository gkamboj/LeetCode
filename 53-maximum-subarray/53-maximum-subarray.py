class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxSum, currSum = -1000000, 0
        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)
            if(currSum < 0): currSum = 0
        return maxSum
#This approach is Kadane's algorithm
#See Java solution for divide and conquer