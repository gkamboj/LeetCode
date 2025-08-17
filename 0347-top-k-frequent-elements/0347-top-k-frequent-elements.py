class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        if len(freq) == k:
            return list(freq.keys())
        temp, result = [[] for i in range(len(nums))], []
        for key, val in freq.items():
            temp[val - 1].append(key)
        while len(result) < k:
            result += temp.pop()
        return result
