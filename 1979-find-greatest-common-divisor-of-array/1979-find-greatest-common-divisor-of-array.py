class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minVal, maxVal = min(nums), max(nums)
        return self.gcd(minVal, maxVal)
        
    def gcd(self, a, b):
        while b > 0: 
            r = a % b
            a = b
            b = r
        return a