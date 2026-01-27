class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 #both pointers start from zero index
        while nums[slow] != nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow, fast = 0, nums[nums[fast]] #move back start to head (zero index), keep fast at collision point of start and fast
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
'''
Approach: 2-pointers using Floyd's cycle/Hare-Tortoise algorithm. Refer following:
1. https://keithschwarz.com/interesting/code/?dir=find-duplicate
2. https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.

See video from 9:00 for proof of Floyd's algorithm: https://www.youtube.com/watch?v=wjYnzkAhcNk or check the LC-142 solution with PDF.
'''
