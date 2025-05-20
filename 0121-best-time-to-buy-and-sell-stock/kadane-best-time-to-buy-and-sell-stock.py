class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, currSum = 0, 0
        
        for ind in range(1, len(prices)):
            currSum += prices[ind] - prices[ind - 1]
            ans = max(currSum, ans)
            if currSum < 0: currSum = 0
        
        return ans
    
# Approach: This is based on Kadane's algorithm -> Assume an imaginary array containing difference 
# of consecutive prices as the elements. Now, finding maximum sum subarray will give the max profit.
# Refer for detail: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
# e.g. 7, 1, 5, 3, 6, 4 -> 0, -6, 4, -2, 3, -2 => max sum subarray = [4, -2, 3] => profit = sum = 5

# See other submissions for other approaches
