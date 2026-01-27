class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while nums[slow] != nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow, fast = 0, nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow