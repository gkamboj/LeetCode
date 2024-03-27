class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        start, end = 1, x//2
        while start <= end:
            mid = start + (end - start)//2
            val = mid ** 2
            if (mid + 1) ** 2 > x and mid ** 2 <= x:
                return mid
            if val > x:
                end = mid - 1
            else:
                start = mid + 1
        
        