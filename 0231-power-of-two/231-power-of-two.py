class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n - 1) == 0
    
#Approach: if n is power of 2, then (n - 1) will have every bit as 1 and n will have only one bit as 1. Their and will give zero.