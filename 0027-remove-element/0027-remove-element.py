class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for ind, num in enumerate(nums):
            if val != num:
                nums[curr] = num
                curr += 1
        return curr
    
'''
Approach: Iterate over array & maintain curr pointer to place elements whenever valid element is encountered.
'''