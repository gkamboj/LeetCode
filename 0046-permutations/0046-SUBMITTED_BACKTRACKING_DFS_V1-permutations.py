class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, [], [0] * len(nums), result)
        return result

    def helper(self, nums, combo, used, result):
        if len(combo) == len(nums):
            result.append(list(combo))
            return

        for ind in range(len(nums)):
            if used[ind]:
                continue
            combo.append(nums[ind])
            used[ind] = 1
            self.helper(nums, combo, used, result)
            combo.pop()
            used[ind] = 0

'''
Approach: Backtracking DFS
- Build permutations by picking unused elements one by one.  
- Use a `used[]` array to track which elements are already included.  
- Add element → recurse → backtrack (remove + mark unused).  
'''
