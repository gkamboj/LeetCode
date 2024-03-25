class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] *= -1
                
# Approach: NOT ALLOWED as original array is modified, this is just for learning purpose.
# Use the original array as hash to store number already seen before and marking them negative.
# Whenever a negative number is encountered, return that number.