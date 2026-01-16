class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        lst = [[] for i in range(len(nums))]
        for num, freq in freq_map.items():
            lst[freq - 1].append(num)
        ans = []
        for ind in range(len(nums) - 1, -1, -1):
            ans += lst[ind]
            if len(ans) == k:
                return ans
