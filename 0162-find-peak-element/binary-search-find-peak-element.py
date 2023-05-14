class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
    
#Approach: Since we need to find just one peak element (and not all), we can apply binary search. This works because if nums[mid] < nums[mid + 1]
# that means peak has to be on right: either whole array will be increasing (nums[-1] will be peak as (n+1)th element can be assumed as infinity)
# or there will be dip somewhere on right side. Similarly when nums[mid] > nums[mid + 1], peak will be on left.

# Note-1: end = mid is used (and not end = mid + 1) because when nums[mid] >= nums[mid + 1], it's possibility that index mid is our answer, but taking
# end = mid - 1 will discard that possibility. Whereas for start, we are sure that mid index cannot be answer, but (mid + 1) can be, so start = mid + 1

#Note: low <= high, high = (mid - 1) will not work.
#Note: Use conditions low <= high and high = (mid - 1) only when we are not comparing with adjacent elements, else it'll cause index out of bound exception
