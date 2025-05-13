class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        ls = [[] for i in range(len(nums))]
        for num in counter:
            ls[counter[num] - 1].append(num)
        result = []
        for ind in range(len(ls) - 1, -1, -1):
            result += ls[ind]
            if len(result) == k:
                return result