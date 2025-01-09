class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        return [key for key, _ in sorted(freq.items(), key=lambda item:item[1], reverse=True)[:k]]
