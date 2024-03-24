class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for ind in range(len(nums) - 2):
            if ind > 0 and nums[ind] == nums[ind - 1]: continue # ignore ind till new value comes
            
            target = -1 * nums[ind]
            start, end = ind + 1, len(nums) - 1 # starting from (ind + 1) as previous values are already taken care of
            
            while start < end:
                if nums[start] + nums[end] == target:
                    start_val, end_val = nums[start], nums[end]
                    result.append([nums[start], nums[ind], nums[end]])
                    # not using nums[start] == nums[start + 1] as at least one increment of start is needed
                    while start < end and nums[start] == start_val: start += 1
                    while start < end and nums[end] == end_val: end -= 1
                elif nums[start] + nums[end] > target: end -= 1
                else: start += 1
        
        return result
    
# Approach: 2-sum for every value, with added conditions to avooid duplicate checks. Take care of each condition to avoid TLE
