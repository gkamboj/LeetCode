class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for ind, num in enumerate(tickets):
            if ind <= k: ans += min(num, tickets[k])
            else: ans += min(num, tickets[k] - 1)
        return ans