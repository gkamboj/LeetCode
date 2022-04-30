class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            result += [subset + [num] for subset in result]
            
        return result
    
# Approach: This is iterative approach. Initialise the result variable with array of size one with empty list being the only element. Now, for every element in nums, append num to every element of result.
# Illustration: Input: [1, 2, 3], result = [[]]
# num = 1 => result = [[]] + [[1]] = [[], [1]]
# num = 2 => result = [[], [1]] + [[2], [1, 2]] = [[], [1], [2], [1, 2]]
# num = 3 => result = [[], [1], [2], [1, 2]] + [[3], [1, 3], [2, 3], [1, 2, 3]] = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Note-1: This is the first approach of LC official solution (i.e. Cascading)
# Note-2: Result will not be in sorted or lexicographic order