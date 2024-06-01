class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 1
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind - 1]:
                nums[curr] = nums[ind]
                curr += 1
        return curr
    
'''
Approach: Use 2 pointers - one to iterate over every element (ind) and another for current index where 
replacement is to be done (curr). Whenever any element is not equal to its predecessor, set it to nums[curr].
Since only number of unique elements need to be returned, return curr and it represents the number of unique
elements encountered so far.
'''
