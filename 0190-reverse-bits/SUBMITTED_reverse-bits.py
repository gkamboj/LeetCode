class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= ((n >> i) & 1) << (31- i)
        return ans
            
# Approach: Get ith bit and set it to (31 - i)th bit of answer. 
