class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inDict = {}
        for ind, val in enumerate(nums):
            if (target - val) in inDict:
                return [inDict[target - val], ind]
            inDict[val] = ind
            
#Approach: One-pass hash table (3rd approach from solutions)