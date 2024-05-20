class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
'''
Approach: 2-pointers using Floyd's cycle/Hare-Tortoise algo. Refer following:
1. https://keithschwarz.com/interesting/code/?dir=find-duplicate
2. https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.

See video from 9:00 for proof of Floyd's algo: https://www.youtube.com/watch?v=wjYnzkAhcNk
'''
