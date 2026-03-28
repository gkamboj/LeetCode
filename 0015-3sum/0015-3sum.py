class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for ind in range(len(nums) - 2):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            start, end, target = ind + 1, len(nums) - 1, -nums[ind]
            while start < end:
                v1, v2 = nums[start], nums[end]
                if v1 + v2 == target:
                    result.append([v1, v2, -target])
                    while start < end and nums[start] == v1:
                        start += 1
                    while start < end and nums[end] == v2:
                        end -= 1
                elif v1 + v2 > target:
                    end -= 1
                else:
                    start += 1
        return result

