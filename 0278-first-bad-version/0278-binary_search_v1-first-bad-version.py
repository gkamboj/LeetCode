# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return n
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            elif not isBadVersion(mid - 1):
                return mid
            else: right = mid - 1

# Approach-1: Binary search using template-1: https://leetcode.com/explore/learn/card/binary-search       
