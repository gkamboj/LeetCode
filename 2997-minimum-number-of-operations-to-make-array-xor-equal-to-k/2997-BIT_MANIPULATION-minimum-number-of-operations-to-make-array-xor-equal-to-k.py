class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums:
            xor ^= num
        return self.countSetBits(xor)
    
    def countSetBits(self, num):
        count = 0
        while num:
            count += num & 1
            num //= 2
        return count
    
'''
Approach: In order to have XOR of nums equal to k, XOR of nums with k should be zero. So, if all set bits of
XOR(nums) ^ k are reversed, condition will be met. Hence, the answer is number of set bits in XOR(nums) ^ k.
'''
