class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, i = 0, 0
        while i < 32:
            negs, currBitsSet = 0, 0
            for num in nums:
                if num < 0:
                    negs += 1
                    num = abs(num)
                if num & (1 << i) > 0:
                    currBitsSet += 1 
            if currBitsSet % 3 == 1:
                ans += 1 << i
            i += 1
        if negs % 3 == 1:
            ans *= -1
        return ans
        