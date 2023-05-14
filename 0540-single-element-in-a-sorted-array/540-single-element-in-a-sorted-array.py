class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        return nums[start]