class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = maxEndingHere = minEndingHere = nums[0] #maxEndingHere/minEndingHere -> max/min product for subarray ending at current index
        for num in nums[1:]:
            if num < 0:
                maxEndingHere, minEndingHere = minEndingHere, maxEndingHere
            maxEndingHere = max(maxEndingHere * num, num)
            minEndingHere = min(minEndingHere * num, num)
            ans = max(ans, maxEndingHere)
        return ans
#Keep storing maxEndingHere & minEndingHere for every index and updating global max. If current value becomes less than 0, then swap maxEndingHere & minEndingHere (as min will now become max after multiplying with negative number)

#See other submissions for more approaches
