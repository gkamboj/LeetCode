class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for ind in range(len(nums) - 2):
            val = nums[ind]
            if ind > 0 and val == nums[ind - 1]:
                continue
            start, end, target = ind + 1, len(nums) - 1, -1 * val
            while start < end:
                start_val, end_val = nums[start], nums[end]
                if start_val + end_val == target:
                    result.append([val, start_val, end_val])
                    while start < end and start_val == nums[start]:
                        start += 1
                    while start < end and end_val == nums[end]:
                        end -= 1
                elif start_val + end_val > target:
                    end -= 1
                else:
                    start += 1
        return list(result)