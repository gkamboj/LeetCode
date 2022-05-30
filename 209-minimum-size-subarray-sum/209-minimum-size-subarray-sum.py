class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, ans = 1, len(nums), 0
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValidSize(mid, target, nums):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
    
    def isValidSize(self, size, target, arr):
        curr, ans = 0, False
        for i in range(size):
            curr += arr[i]
        for i in range(size, len(arr)):
            if curr >= target:
                ans = True
                break
            curr += arr[i] - arr[i - size]
        return True if curr >= target else ans
    
# Approach: This is binary search approach - start from mid size and go left or right depending on whether the size is valid or not. TC: O(n logn), Space: O(1).