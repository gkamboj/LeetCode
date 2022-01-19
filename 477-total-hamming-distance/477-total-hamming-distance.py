class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            onesCount = 0
            for num in nums:
                if num >> i & 1 == 1:
                    onesCount += 1
            ans += onesCount * (len(nums) - onesCount)
        return ans