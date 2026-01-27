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

'''
Approach: Binary search - minimum speed can be 1, and max can be max(piles). Start from the middle of these
and keep applying binary search till start <= end.

Check this for binary search templates: https://leetcode.com/problems/koko-eating-bananas/discuss/769702/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
'''
