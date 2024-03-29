class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-2**31-1] + nums + [-2**31-1]
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid] >= nums[mid + 1]: right = mid - 1
            else: left = mid + 1