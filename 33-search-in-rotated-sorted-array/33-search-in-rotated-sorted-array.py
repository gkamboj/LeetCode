class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
    
#Approach:
# Binary search with iterations.
# Note-1: Focus on where to use = (i.e. <= and >=) in lines 11 and 16 
# Note-2: changing line-7 condition to start < end will require another check of comparing target with nums[start] after the end of while loop