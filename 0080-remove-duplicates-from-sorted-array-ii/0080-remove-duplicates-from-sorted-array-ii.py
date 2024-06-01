class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, ind = 0, 0
        while ind < len(nums):
            if not ind or nums[ind] != nums[ind - 1]:
                nums[curr] = nums[ind]
                curr += 1
                ind += 1
                if ind < len(nums) and nums[ind] == nums[ind - 1]:
                    nums[curr] = nums[ind]
                    curr += 1
                    ind += 1
            else:
                ind += 1
        return curr