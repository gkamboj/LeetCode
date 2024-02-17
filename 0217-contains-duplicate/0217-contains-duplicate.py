class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = defaultdict(int)
        for num in nums:
            countDict[num] += 1
            if countDict[num] == 2:
                return True
        return False
    
# Approach: defaultdict for default value 0 if key is not present in dictionary