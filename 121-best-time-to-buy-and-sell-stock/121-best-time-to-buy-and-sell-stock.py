class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        
        minPriceYet, ans = prices[0], 0
        for price in prices:
            minPriceYet = min(minPriceYet, price)
            currProfit = price - minPriceYet
            ans = max(currProfit, ans)
        return ans
    
#Approach: For every price, update minimum price till now (if it's lesser than min price) and find profit. Update global profit accordingly.

#See other submissions for other approaches