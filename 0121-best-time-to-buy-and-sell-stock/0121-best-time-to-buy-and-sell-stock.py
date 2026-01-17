class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, curr_min = 0, 10**4 + 1
        for price in prices:
            curr_min = min(price, curr_min)
            ans = max(ans, price - curr_min)
        return ans