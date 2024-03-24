class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for ind in range(len(nums) - 2):
            target = -1 * nums[ind]
            start, end = ind + 1, len(nums) - 1
            while start < end:
                if start == ind: start += 1
                elif end == ind: end -= 1
                elif nums[start] + nums[end] == target:
                    result.add(tuple(sorted([nums[ind], nums[start], nums[end]])))
                    while start < end and nums[start] == nums[start + 1]: start += 1
                    while start < end and nums[end] == nums[end - 1]: end -= 1
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > target: end -= 1
                else: start += 1
        return result