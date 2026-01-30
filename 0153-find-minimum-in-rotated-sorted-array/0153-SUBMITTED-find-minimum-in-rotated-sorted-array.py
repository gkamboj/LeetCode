class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            print("start: ", start, ", mid ", mid, ", end ", end)
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]

# Approach: Binary search. Note that `nums[start]` is returned at the end to handle cases when `mid`
# becomes the same as `start` due to integer division.

# Check Neetcode for a solution with an alternative terminating condition.
