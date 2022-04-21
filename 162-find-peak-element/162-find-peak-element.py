class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
    
#Approach: Since we need to find just one peak element (and not all), we can apply binary search. This works because if nums[mid] > nums[mid + 1], that means peak has to be on left: either whole array will be decreasing (nums[0] will be peak) or there will be dip somewhere on left side. Similarly when nums[mid] < nums[mid + 1], peak will be on right.