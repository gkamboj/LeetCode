class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minVal, maxVal = nums[0], nums[0]
        for num in nums:
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
        
        while minVal > 0:
            rem = maxVal % minVal
            maxVal = minVal
            minVal = rem
        
        return maxVal