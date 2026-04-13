class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums, ind, result):
        if ind == len(nums):
            result.append(list(nums))
            return

        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.helper(nums, ind + 1, result)
            nums[ind], nums[i] = nums[i], nums[ind]
            
'''
Approach: Backtracking DFS with swapping
- Fix one index at a time by swapping the current element with all possible choices.  
- Recurse for next index, then swap back to restore state.  
- Avoids extra space.

Refer to the video for details: https://youtu.be/f2ic2Rsc9pU
'''
