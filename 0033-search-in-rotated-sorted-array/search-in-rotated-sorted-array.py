class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] > nums[high]:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return ans
    
# Approach: Binary search approach - find mid and use value at mid to check if pivot is on left or right:
# 1. If pivot is on right: if target lies between nums[start] and nums[mid] that is if target lies in left part which is monotonically increasing half of array then set high to (mid - 1). If not, that means target lies in pivot half => so set low to (mid + 1)
# 2. If pivot is on half: if target lies between nums[mid] and nums[end] that is if target lies in right part which is monotonically increasing half of array then set low to (mid + 1). If not, that means target lies in pivot half => set high to (mid - 1)

# Note-1: Since there is no comparison with adjacent elements in main method, minMat <= maxMat is used (and not minMat < maxMat).
#Note-2: Observe that <=, >= is used (instead of just <, >) while comparing nums[mid] with nums[start] and nums[end] because end points can also be answers.
