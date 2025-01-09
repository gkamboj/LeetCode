class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                return True
        return False

# Approach: defaultdict for default value 0 if key is not present in dictionary