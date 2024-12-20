class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for ind, num in enumerate(nums):
            if (target - num) in hm:
                return [ind, hm[target - num]]
            hm[num] = ind

#Approach: One-pass hash table (3rd approach from solutions)
