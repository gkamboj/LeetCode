class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, i, negs = 0, 0, 0
        for ind, num in enumerate(nums):
            if num < 0:
                nums[ind] = -1*num
                negs += 1
        while i < 32:
            currBitsSet = 0
            for num in nums:
                if num & (1 << i) > 0:
                    currBitsSet += 1 
                    currBitsSet %= 3
            if currBitsSet == 1:
                ans |= 1 << i
            i += 1
        if negs % 3 == 1:
            ans *= -1
        return ans
        