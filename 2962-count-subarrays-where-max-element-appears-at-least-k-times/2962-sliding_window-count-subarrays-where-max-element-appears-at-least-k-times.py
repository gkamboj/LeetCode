class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val, count = max(nums), 0
        ans, start = 0, 0
        for ind in range(len(nums)):
            if nums[ind] == max_val:
                count += 1
                if count == 1: start = ind
            
            while count > k:
                start += 1
                if nums[start] == max_val:
                    count -= 1
                
            if count == k:
                ans += start + 1
        return ans
    
# Approach: Sliding window -> Maintain a start pointer and end pointer so that frequency of max element b/w
# these indices (both included) is k. Whenever end points to max element, add (start + 1) to answer as no.
# of subarrays including start and end indices will be (start + 1): 'start' no. of subarrays starting before
# 'start' index and another [start, end]
