class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        if len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start