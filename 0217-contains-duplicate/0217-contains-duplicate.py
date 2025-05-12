class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_map = defaultdict(int)
        for num in nums:
            dict_map[num] += 1
            if dict_map[num] > 1:
                return True
        return False