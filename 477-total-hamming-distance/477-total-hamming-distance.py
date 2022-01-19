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
    
#Approach: Observe that sum of pairwise hamming distance is same as sum of x*y for every bit, where x = number of set bits and y = number of unset bits.