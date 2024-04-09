class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for ind, num in enumerate(tickets):
            if ind <= k: ans += min(num, tickets[k])
            else: ans += min(num, tickets[k] - 1)
        return ans
    
''' Approach: In order to buy all tickets at index k, min of the tickets at index and tickets at index k
should be bought for every index <= k. Similarly, for indices > k, min of tickets at index and one less than 
tickets at index k should be bought.
'''
