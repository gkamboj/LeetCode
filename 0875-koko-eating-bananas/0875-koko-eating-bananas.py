class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        ans = high = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            hours = self.eatingHours(piles, mid)
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1
                ans = min(ans, mid)
        return ans


    def eatingHours(self, piles, speed):
        hours = 0
        for count in piles:
            hours += -(-count//speed)
        return hours