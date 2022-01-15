class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, i = 0, 0
        while i < 32:
            negs, currBitsSet = 0, 0
            for num in nums:
                if num < 0:
                    negs += 1
                    num = abs(num)
                if num & (1 << i) == (1 << i):
                    currBitsSet += 1 
            if currBitsSet % 3 == 1:
                ans += 1 << i
            i += 1
        if negs % 3 == 1:
            ans *= -1
        return ans

#Approach: For every 32 bits, count number of set bits. If it's not multiple of 3, then this bit is set for our answer. Find every set bit of answer.

#Note-1: We are handling negative numbers separately because Python does not have int limit. Even if our answer value goes above (2^31 - 1), it does not change to negative. In Java, INT_MAX + 1 = INT_MIN
#Note-2: See Java solution, which runs without handling of negative cases.