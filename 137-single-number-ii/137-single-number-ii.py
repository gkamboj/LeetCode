class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, negCount = 0, 0
        for i in range(32):
            setBits = 0
            for num in nums:
                if num < 0:
                    num = abs(num)
                    negCount += 1
                setBits += (num >> i) & 1
            ans |= (setBits % 3) << i
        if negCount % 3 != 0:
            ans = -1 * ans
        return ans

#Approach: For every 32 bits, count number of set bits. If it's not multiple of 3, then this bit is set for our answer. Find every set bit of answer.

#Note-1: We are handling negative numbers separately because Python does not have int limit. Even if our answer value goes above (2^31 - 1), it does not change to negative. In Java, INT_MAX + 1 = INT_MIN
#Note-2: See Java solution, which runs without handling of negative cases.
