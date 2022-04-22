class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 1 and nums[mid] == nums[mid + 1]) or (mid % 2 == 0 and nums[mid] == nums[mid - 1]):     
                high = mid
            else:
                low = mid + 1
        return nums[low]
    
# Approach: As the array is sorted, binary search can be applied. For deciding condition, observe that every poir will start at even index till the single element is not encountered. Once the single element is encountered, every pair will start at odd index. From this we can conclude when to search towards right (and hence making low = mid + 1).
# Note-1: User high = mid and low < high in while loop (not high = mid - 1 and low <= high)