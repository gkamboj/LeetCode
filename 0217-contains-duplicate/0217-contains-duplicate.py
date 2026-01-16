class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if seen[num] == 1:
                return True
            seen[num] += 1
        return False