class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit
            
'''
Approach: This is sliding window approach. Refer for more detail: https://youtu.be/1pkOgXD63yU

Check other submissions for more approaches
'''
