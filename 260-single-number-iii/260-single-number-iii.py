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