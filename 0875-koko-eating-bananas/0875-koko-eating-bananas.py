class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end, ans = 1, max(piles), max(piles)
        while start <= end:
            mid = start + (end - start) // 2
            hours = self.findEatingHours(piles, mid)
            if hours > h:
                start = mid + 1
            else:
                end = mid - 1
                ans = min(ans, mid)
        return ans
    
    
    def findEatingHours(self, piles, speed):
        val = 0
        for pile in piles:
            val += -(pile // -speed)
        return val