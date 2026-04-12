class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, ind, subset, result):
        if ind == len(nums):
            result.append(list(subset))
            return

        self.helper(nums, ind + 1, subset, result)

        subset.append(nums[ind])
        self.helper(nums, ind + 1, subset, result)
        subset.pop()

'''
Approach: Backtracking (DFS - Pick / Not Pick)
- At each index, make two choices: include the element or skip it.
- Recurse to the next index in both cases.
- When index reaches end, add a copy of current subset to result.
- Use append/pop to build subsets in-place (backtracking).
- This forms a binary decision tree of size 2^n.

- Optimal approach:
  - Generates all subsets (2^n), which is required.
  - Time: O(2^n * n), Space: O(n) recursion depth.
'''
