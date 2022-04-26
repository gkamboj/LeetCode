class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            sets = []
            for subset in result:
                newSubset = subset[:]
                newSubset.append(num)
                sets.append(newSubset)
            result += sets
            
        return result