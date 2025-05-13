import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high, ans = 1, max(piles), 0
        while low <= high:
            mid = low + (high - low) // 2
            hours = self.calculate_hours(piles, mid)
            if hours <= h:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

    def calculate_hours(self, piles, speed):
        hours = 0
        for count in piles:
            hours += math.ceil(count / speed)
        return hours