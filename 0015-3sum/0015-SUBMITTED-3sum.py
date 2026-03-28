class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for ind in range(len(nums) - 2):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue # ignore ind till new value comes
            
            target = -nums[ind]
            start, end = ind + 1, len(nums) - 1 # starting from (ind + 1) as previous values are already taken care of
            
            while start < end:
                v1, v2 = nums[start], nums[end]
                if nums[start] + nums[end] == target:
                    result.append([v1, -target, v2])
                    # not using nums[start] == nums[start + 1] as at least one increment of start is needed
                    while start < end and nums[start] == v1:
                        start += 1
                    while start < end and nums[end] == v2:
                        end -= 1
                elif v1 + v2 > target:
                    end -= 1
                else:
                    start += 1
        
        return result
    
# Approach: 2-sum for every value, with added conditions to avoid duplicate checks.
# Take care of each condition to avoid TLE
