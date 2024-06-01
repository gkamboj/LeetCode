class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        start, end = -1, -1
        for ind, num in enumerate(nums):
            if num == val:
                if start == -1:
                    start = ind
                end = ind
            if num > val:
                break
        if start == -1:
            return len(nums)
        ind = end + 1
        while ind < len(nums):
            nums[start] = nums[ind]
            ind += 1
            start += 1
        return start