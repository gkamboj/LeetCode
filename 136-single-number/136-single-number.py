class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    
# Approch: Since x ^ x = 0, taking the XOR of entire array will cancel out every element except the required element.