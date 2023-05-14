class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicesDict = {}
        for (ind, num) in enumerate(nums):
            if (target - num) in indicesDict:
                return [indicesDict[target - num], ind]
            indicesDict[num] = ind