class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] += 1
        if len(freqDict) == k:
            return freqDict.keys()
        else:
            result = []
            freqList = [[] for i in range(len(nums))]
            for key, val in freqDict.items():
                freqList[val - 1].append(key)
            for ls in freqList[::-1]:
                if len(result) < k:
                    result += ls
                else:
                    return result
                    
