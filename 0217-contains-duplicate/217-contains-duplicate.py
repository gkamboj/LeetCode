class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = dict()
        for num in nums:
            if num in numsDict: return True
            numsDict[num] = 1
        return False
    
    #Other approaches:
    #1. Sort nums -> no extra space but O(n lg n)
    #2. Use set instead of dictionary: same space and memory
        