class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            print(mid)
            if nums[mid - 1] > nums[mid]:  
                return nums[mid]
            
            if nums[left] < nums[mid] < nums[right]:
                right = mid - 1  
                
            elif nums[left] <= nums[mid] > nums[right]:
                left = mid + 1
                
            elif nums[left] > nums[mid] < nums[right]:
                right = mid - 1