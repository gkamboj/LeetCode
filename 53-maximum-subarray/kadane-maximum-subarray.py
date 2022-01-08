class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        maxSum, currSum = -1000000, 0
        tempStart, start, end = 0, 0, 0
        for ind, num in enumerate(nums):
            currSum += num
            if maxSum < currSum:
                maxSum = currSum
                end = ind
                start = tempStart
            if(currSum < 0):
                currSum = 0
                tempStart = ind + 1
        return maxSum
#This approach is Kadane's algorithm and also gives start as well as end index of subarraya
#See Java solution for divide and conquer
