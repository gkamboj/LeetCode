class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        start, end = 0, len(nums) - 1
        while True:
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1

#Approach: Binary search.

#Check other submissions for more approaches.