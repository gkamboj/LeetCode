class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [nums[0]] #dp[i] -> max sum subarray ending at index i 
        maxSum = nums[0]
        for num in nums[1:]:
            dp.append(max(num, num + dp[-1]))
            maxSum = max(maxSum, dp[-1])
        return maxSum
    
#This approach is using DP. dp[i] represents the maximum possible sum of subarray which is ending at index i.
#Refer other submissions for more approaches

#See https://github.com/gkamboj/LeetCode/blob/main/PyDSCodes/ds/arrays/questions/MaximumSumSubarray.py if start and end index of array are also needed.
