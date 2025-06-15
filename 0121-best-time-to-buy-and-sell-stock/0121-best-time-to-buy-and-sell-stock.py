class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end, ans = 0, 0, 0
        while end < len(prices):
            if prices[end] >= prices[start]:
                ans = max(prices[end] - prices[start], ans)
            else:
                start = end
            end += 1
        return ans
            