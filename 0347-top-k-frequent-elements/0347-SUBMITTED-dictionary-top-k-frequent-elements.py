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

# Approach: Create a list of lists to store the nums elements for every frequency, with the index of list acting as the frequency value.
# Refer for more detail: https://leetcode.com/problems/top-k-frequent-elements/discuss/81602/Java-O(n)-Solution-Bucket-Sort
