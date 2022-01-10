class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_rotated_index(nums,low,high,n):
            if low <= high:
                mid = (low + high) // 2
                if mid + 1 <= n and nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[low]:
                        return find_rotated_index(nums,low,mid-1,n)
                    else:
                        return find_rotated_index(nums,mid+1,high,n)
                    
            return -1
        
        rotated_index = find_rotated_index(nums,0,len(nums)-1,len(nums)-1)
        if rotated_index == -1:
            return nums[0]
        else:
            return min(nums[0],nums[rotated_index])