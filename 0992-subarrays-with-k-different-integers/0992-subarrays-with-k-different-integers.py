class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostK(nums, k) - self.subarraysWithAtMostK(nums, k - 1)
    
    def subarraysWithAtMostK(self, nums, k):
        freq_dict, start, count = defaultdict(int), 0, 0
        
        for ind in range(len(nums)):
            freq_dict[nums[ind]] += 1
            
            while len(freq_dict) > k:
                freq_dict[nums[start]] -= 1
                if not freq_dict[nums[start]]: del freq_dict[nums[start]]
                start += 1
            
            count += ind - start + 1
        
        return count