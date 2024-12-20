class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for ind, num in enumerate(nums):
            if (target - num) in hm:
                return [hm[target - num], ind]
            hm[num] = ind