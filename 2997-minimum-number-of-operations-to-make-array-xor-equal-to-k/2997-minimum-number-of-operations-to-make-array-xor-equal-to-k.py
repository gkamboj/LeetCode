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