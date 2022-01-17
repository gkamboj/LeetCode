class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        first, second = 0, 0
        singleAppXor = 0
        for num in nums:
            singleAppXor ^= num
        xorWithRightestBitSet = singleAppXor - (singleAppXor & (singleAppXor - 1))
        for num in nums:
            if xorWithRightestBitSet & num == xorWithRightestBitSet:
                first ^= num
        second = singleAppXor ^ first
        return [first, second]
    
#Approach: Take XOR over the array. This will give the XOR of two numbers appearing once, say it to be singleAppXor. Find the rightmost set bit in singleAppXor, this bit will make sure one of the answer element has that bit as 0 and other as 1. Now, nums can be divided into two parts: one with that bit as set and other part having that bit as unset. Iterate over the one part of array (using condn in Line-9) and find one answer. Once we have an answer, other answer can be found out.

#Note-1: Line-7 is giving us the number which is having only rightmost set bit, rest all 0s. 