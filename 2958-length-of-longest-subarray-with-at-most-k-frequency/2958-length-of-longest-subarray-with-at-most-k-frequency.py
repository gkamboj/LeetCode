class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        freq_dict, start, ans = defaultdict(int), 0, 0
        for ind, num in enumerate(nums):
            if freq_dict[num] == k:
                while True:
                    val = nums[start]
                    freq_dict[nums[start]] -= 1
                    start += 1
                    if val == num:
                        break
            freq_dict[num] += 1
            ans = max(ans, ind - start + 1)
        return ans