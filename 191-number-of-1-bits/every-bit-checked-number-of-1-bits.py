class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count
    
#Approach: Check for rightmost bit and increase count if it's set. Rightshift the n by 1 bit, Continue till n > 0. TC -> O(number of bits in N)

#See https://leetcode.com/problems/number-of-1-bits/discuss/55099/Simple-Java-Solution-Bit-Shifting to understand difference if working in Java

#See other approach for a little optimised solution
