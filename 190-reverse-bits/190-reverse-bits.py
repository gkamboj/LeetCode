class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans | ((n >> i) & 1)) << 1
        return ans >> 1
    
# Approach: Get ith bit and add it to the answer, then shift answer towards left by 1 bit (so that next iteration's ith bit is added at list). While returning, right shift by 1 bit because answer is left shifted one time extra.