class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, ind, subset, result):
        if ind == len(nums):
            result.append(list(subset))
            return

        subset.append(nums[ind])
        self.helper(nums, ind + 1, subset, result)
        subset.pop()
        
        while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
            ind += 1
        self.helper(nums, ind + 1, subset, result)

'''
Approach: Backtracking + DFS
- Sort the array so duplicates are adjacent, making them easier to handle.
- Use backtracking: for each index, explore both possibilities (including and excluding current index element).
- To handle duplicates, for the exclude case, skip all duplicates of the current number before recursing.
'''
