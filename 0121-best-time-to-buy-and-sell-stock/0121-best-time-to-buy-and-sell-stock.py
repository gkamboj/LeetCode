class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, max(prices), min(prices)
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit