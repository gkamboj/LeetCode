class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            result += [subset + [num] for subset in result]
        
        return result

'''
Approach: Iterative (Functional / Doubling)
- Start with result = [[]].
- For each number, generate new subsets by adding it to every existing subset.
- Append all new subsets back into result in one step.
- This doubles the number of subsets at each iteration.
- Final result contains all 2^n subsets.

- Time: O(2^n * n)
- Space: O(2^n)

- Key idea: each element “copies” all existing subsets and expands them.
'''