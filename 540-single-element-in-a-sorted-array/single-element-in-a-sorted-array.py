class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 1 and nums[mid] == nums[mid + 1]) or (mid % 2 == 0 and nums[mid] == nums[mid - 1]):     
                high = mid - 1
            else:
                low = mid + 1
        return nums[low]
    
# Approach: As the array is sorted, binary search can be applied. For deciding condition, observe that every poir will start at even index till the single element is not encountered. Once the single element is encountered, every pair will start at odd index. From this we can conclude when to search towards right (and hence making low = mid + 1).

# Note-1: Observe we have used high = mid - 1. Give a little thought to understand that when line-8 if condition is fulfilled, high cannot be mid, it can be max mid - 1.
# Note-2: To avoid index out of bound exception, use low <= high only if we're not doing comparison with adjacent elements
