class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        freq_dict, start, ans = defaultdict(int), 0, 0
        for ind in range(len(nums)):
            freq_dict[nums[ind]] += 1
            while freq_dict[nums[ind]] > k:
                freq_dict[nums[start]] -= 1
                start += 1
            ans = max(ans, ind - start + 1)
        return ans