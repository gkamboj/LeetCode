class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= ((n >> i) & 1) << (31- i)
        return ans
            
# Approach: Get ith bit and set it to (31 - i)th bit of answer. 
# Getting the ith bit: b = (n >> i) & 1.
# Setting this bit to (31 - i)th bit of answer: ans != b << (31 - i)
