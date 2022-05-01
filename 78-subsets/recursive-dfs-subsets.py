class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsetsRecursively(nums, [], result)
        return result
    
    def subsetsRecursively(self, nums, subset, result):
        result.append(subset)
        for i in range(len(nums)):
            self.subsetsRecursively(nums[i + 1:], subset + [nums[i]], result)
    
# Approach: This is recursive approach using DFS. Start with first element of array and find all subsets starting with that element. After that repeat the process for subsequent elements. Since there are 2^n subsets which we need to find, TC: O(2^n)

# Reference: https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS)

# Dry Run:
# subsetsRecursively([1, 2, 3], [], [])
# i = 0 => subsetsRecursively([2, 3], [1], [[]])
#       i' = 0 => subsetsRecursively([3], [1, 2], [[], [1]])
#              i'' = 0 =>  subsetsRecursively([], [1, 2, 3], [[], [1], [1, 2]])
#       i' = 1 => subsetsRecursively([], [1, 3], [[], [1], [1, 2], [1, 2, 3]]) //in current level, subset was [1] => 2nd parameter = [1] + [3] = [1, 3]
# i = 1 => subsetsRecursively([3], [2], [[], [1], [1, 2], [1, 2, 3], [1, 3]])
#       i' = 0 => subsetsRecursively([], [2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]])
# i = 2 => subsetsRecursively([], [3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]])
# => result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# Note: This approach returns solution is sorted as well as lexicographic order.
