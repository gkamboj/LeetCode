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
    
# Approach: This is iterative solution similar to iterative approach of LC-78. To handle duplicates, append num to only those subsets which were appended in last iteration when num is duplicate. 