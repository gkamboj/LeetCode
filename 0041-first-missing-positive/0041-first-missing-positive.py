class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_present = False
        
        for ind, num in enumerate(nums):
            one_present = one_present or num==1
            if num <= 0 or num > len(nums):
                nums[ind] = 1
        
        if not one_present: return 1

        for ind, num in enumerate(nums):
            if nums[abs(num) - 1] > 0: # Check only positives to avoid repeated processing of duplicates
                nums[abs(num) - 1] *= -1
            
        for ind in range(len(nums)):
            if nums[ind] > 0: return ind + 1
        
        return len(nums) + 1
    
# Approach: Since no extra space is allowed, we are modifying the original array to use it as hash.
# S-1: As -ve and values more than size of array are of no use**, replace them by 1s. This will make
# sure every value in nums is between 1 and n (len(nums)).
# S-2: While doing S-1, check if 1 is present or not. If 1 is not present, return 1
# S-3: Traverse over nums and make nums[ind] negative for every ind to represent ind is present in nums.
# Take care of duplicates while doing this.
# S-4: Return the first +ve from the nums after S-3. If there is no +ve, return len(nums) + 1**

# Note-1: ** -> If no answer is found in first n values (size of array), then answer has to be (n + 1)
# as our aim is to get smallest positive not in array
# Note-2: Refer approach-2 from official solution for better understanding