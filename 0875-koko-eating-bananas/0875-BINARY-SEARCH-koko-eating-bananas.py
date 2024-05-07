class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end, ans = len(piles), max(piles), max(piles)
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

'''
Approach: Binary search - minimum hours can be len(piles) [when speed = max(piles)] and max can be max(piles) [when speed = 1]. Start from mid of these
and keep applying binary search till start <= end.

Check this for binary search templates: https://leetcode.com/problems/koko-eating-bananas/discuss/769702/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
'''
