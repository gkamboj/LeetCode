class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_ind = start_ind = end_ind = -1
        ans = 0
        for ind, val in enumerate(nums):
            if val < minK or val > maxK: bad_ind = ind
            if val == minK: start_ind = ind
            if val == maxK: end_ind = ind
            ans += max(0, min(start_ind, end_ind) - bad_ind)
        return ans
    
'''
Approach: For every iteration, find 3 variables to store last bad index (where value is outside thhe [minK, 
maxK] range, last start index (where value is minK), last end index (where value is maxK). Total number of
subarrays from these can be found as -> min(start_ind, end_ind) - bad_ind. We are taking min here because:
take a case [0, 1, 2, 3, 4, 5, 6, 7] with minK = 4, maxK = 6, bad_ind = 1, start_ind = 4, end_ind = 6. No 
matter what, [4, 5, 6] will always be part of subarrays due to given bounds, and other possibilities are 
[3, 4, 5, 6] and [2, 3, 4, 5, 6]. This can be found by taking starting index of required subarray ([4, 5, 6]),
that is 4. So, answer for this iteration will be min(4, 6) - 1 = 3. To avoid negative count, another check has
been added to compare with 0.

Note: Remember to use all if conditions instead of else to handle cases where minK and maxK are same.
'''