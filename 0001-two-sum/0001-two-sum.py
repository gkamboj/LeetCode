class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map = {}
        for ind, val in enumerate(nums):
            if (num:=(target - val)) in ind_map:
                return [ind_map[num], ind]
            ind_map[val] = ind