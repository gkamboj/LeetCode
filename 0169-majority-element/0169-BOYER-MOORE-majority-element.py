class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ans = 0, nums[0]
        for num in nums[1:]:
            if ans == num:
                count += 1
            elif count == 0:
                ans = num
            else:
                count -= 1
        return ans
    
'''
Approach: This is based on Boyer Moore algorithm (https://www.cs.utexas.edu/~moore/best-ideas/mjrty/).
'''
