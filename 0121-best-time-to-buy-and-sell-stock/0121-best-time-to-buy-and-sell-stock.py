class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 0
        ans, profit = 0, 0
        while end < len(prices):
            if prices[end] >= prices[start]:
                profit = prices[end] - prices[start]
                end += 1
                ans = max(profit, ans)
            else:
                start += 1
        return ans
            