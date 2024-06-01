class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, k = 0, 2
        for num in nums:
            if curr < k or num > nums[curr - k]:
                nums[curr] = num
                curr += 1
        return curr
    
'''
Approach: Generic solution for any similar question to have unique elements at most k times.

Reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/27976/3-6-easy-lines-c-java-python-ruby/
'''