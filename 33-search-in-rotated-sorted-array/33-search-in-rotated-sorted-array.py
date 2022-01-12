class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[mid] < nums[end]:
                if nums[mid] < target and nums[end] > target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target and nums[start] < target:
                    end = mid - 1
                else:
                    start = mid + 1
        if nums[start] == target:
            return start
        return -1