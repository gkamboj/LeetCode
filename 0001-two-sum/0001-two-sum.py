class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map = {}
        for ind, num in enumerate(nums):
            if (target - num) in ind_map:
                return [ind, ind_map[target - num]]
            ind_map[num] = ind