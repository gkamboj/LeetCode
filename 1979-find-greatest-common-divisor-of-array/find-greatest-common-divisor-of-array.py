class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minVal, maxVal = nums[0], nums[0]
        for num in nums:
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
        
        return self.findGCDRecursive(minVal, maxVal)
    
    def findGCDRecursive(self, num1, num2):
        if num2 == 0:
            return num1
        return self.findGCDRecursive(num2, num1 % num2)
    
    def findGCDIterative(self, num1, num2):
        while num2 > 0:
            rem = num1 % num2
            num1 = num2
            num2 = rem
        return num1
    
#Approach: Euclid Algorithm -> GCD(a, b) = GCD(b, a % b) = GCD(a % b, b). This has been implemented through both iterative and recursive ways.
