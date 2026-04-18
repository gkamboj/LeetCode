class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, prev = [[]], -11 # take any value outside the bounds to start
        nums.sort()
        
        for num in nums:
            if num == prev:
                target = curr
            else:
                target = result
            
            curr = [subset + [num] for subset in target]
            result += curr
            prev = num

        return result
        

'''
Approach: Iteration

- If there were no duplicates, we would be doing:
    - Start with result = [[]].
    - For each number, generate new subsets by adding it to every existing subset.
    - Append all new subsets back into result in one step.
    - This doubles the number of subsets at each iteration.
    - Final result contains all 2^n subsets.

- To handle duplicates:
    - Sort the array so duplicates are adjacent, making them easier to handle.
    - When current num is duplicate (same as previous number), append num to only those subsets which were appended in last iteration.
    - When num is not duplicate, append num to all subsets present in `result` so far.
'''
