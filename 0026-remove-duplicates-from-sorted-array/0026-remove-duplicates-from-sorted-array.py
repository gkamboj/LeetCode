class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        curr, ind, n = 0, 0, len(nums)
        while ind < n - 1:
            val = nums[ind]
            while ind < n -1 and nums[ind] == nums[ind + 1]:
                ind += 1
            nums[curr] = val
            curr += 1
            ind += 1
        if nums[-1] != nums[-2]:
            nums[curr] = nums[-1]
            curr += 1
        return curr