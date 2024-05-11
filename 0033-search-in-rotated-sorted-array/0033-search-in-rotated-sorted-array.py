class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
    
'''
Approach: Binary search approach - find mid and use value at mid to check if pivot is on left or right:

1. If pivot is on right: if target lies between nums[start] and nums[mid] that is if target lies in left part 
which is monotonically increasing half of array then set end to (mid - 1). If not, that means target lies in 
right half => so set start to (mid + 1)

2. If pivot is on left: if target lies between nums[mid] and nums[end] that is if target lies in right part 
which is monotonically increasing half of array then set start to (mid + 1). If not, that means target lies 
in pivot half => set end to (mid - 1)

Note:
1. There's "nums[start] <= nums[mid]" on line 10, and not "nums[start] < nums[mid]"
2. There's "nums[start] <= target < .." and ".. < target <= nums[end]" on lines 11 and 16 respectively, that 
is with = sign because these end values can also be answers
'''
