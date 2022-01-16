class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for ind, num in enumerate(nums):
            ans ^= ind ^ num
        return ans
    
#Approach: Since numbers are from 0 to n (except a number missing) and indexes are from 0 to (n - 1), XOR every number and index. Every repition cancels out leaving missing number at end.

#See other submission for approach without using XOR