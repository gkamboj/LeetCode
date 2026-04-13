class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        for num in nums:
            temp = []
            for combo in ans:
                temp.extend(self.expand_permutations(combo, num))
            ans = temp
        
        return ans

    def expand_permutations(self, arr, num):
        result = []
        for i in range(len(arr) + 1):
            result.append(arr[:i] + [num] + arr[i:])
        return result

'''
Approach: Iterative BFS
- Build permutations iteratively by inserting each new number into all positions of existing permutations.  
- Start with the first element, then for every next number, generate new lists by placing it at every index.  
- Use a temporary list to store newly formed permutations at each step.  
- Update the answer list after processing each element.
'''