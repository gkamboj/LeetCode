class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid - 1]) or (mid % 2 == 1 and nums[mid] == nums[mid + 1]):
                high = mid
            else:
                low = mid + 1
        return nums[low]