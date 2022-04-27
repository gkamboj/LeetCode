class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, prev = [[]], -11
        nums.sort()
        for num in nums:
            if num != prev:
                sets = [subset + [num] for subset in result]
            else:
                sets = [subset + [num] for subset in sets]
            result += sets
            prev = num
        return result