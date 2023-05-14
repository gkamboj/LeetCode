class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end, ans = 0, len(nums) - 1, -1
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return ans