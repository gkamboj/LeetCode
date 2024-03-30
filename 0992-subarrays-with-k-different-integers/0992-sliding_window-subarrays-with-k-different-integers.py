class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostK(nums, k) - self.subarraysWithAtMostK(nums, k - 1)
    
    def subarraysWithAtMostK(self, nums, k):
        count, start, freq_dict = 0, 0, defaultdict(int)
        
        for ind in range(len(nums)):
            freq_dict[nums[ind]] += 1
            
            while len(freq_dict) > k:
                freq_dict[nums[start]] -= 1
                if not freq_dict[nums[start]]:
                    del freq_dict[nums[start]]
                start += 1
            
            count += ind - start + 1
        
        return count
    
# Approach: Sliding window -> For each window, calculate the total number of subarrays it can form by formula
# (ind - left + 1). This represents the number of subarrays ending at the current element (ind) and starting 
# anywhere from the current left boundary (left) to the right pointer (right) (inclusive). Once the window 
# contains more than k distinct elements, start shrinking it from the left side. Remove the element at the 
# leftmost position and update the set of distinct elements. This process continues until the window size 
# becomes valid again for the condition. Since this returns count of subarrays containing less than or equal
# to k distinct elements, subtract the corresponding count for (k - 1).

# Refer approach-1 of official solution for more detail.
