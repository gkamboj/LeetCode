import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 # minimum speed
        high = ans = max(piles)
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
        val = 0
        for pile in piles:
            val += -(pile // -speed)
        return val

    def eatingHoursV2(self, piles, speed):
        hours = 0
        for count in piles:
            hours += math.ceil(count / speed)
        return hours

