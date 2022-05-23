class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        return self.solve(nums)
    
    def solve(self, nums):
        if len(nums) == 1:
            return [[nums[0]], []]
        
        result = []
        
        num = nums.pop(0)
        subsets = self.solve(nums)
        result += subsets
        result += [subset + [num] for subset in subsets]
        
        return result
            
        
        