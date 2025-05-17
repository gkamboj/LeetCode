class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr, ans = nums[0], []
        for ind in range(len(nums) - 2):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            start, end = ind + 1, len(nums) - 1
            target = -1 * nums[ind]
            while start < end:
                total = nums[start] + nums[end]
                if total == target:
                    ans.append([nums[ind], nums[start], nums[end]])
                    s_val, e_val = nums[start], nums[end]
                    # start += 1
                    # end -= 1
                    while start < end and nums[start] == s_val:
                        start += 1
                    while start < end and nums[end] == e_val:
                        end -= 1
                elif total > target:
                    end -= 1
                else:
                    start += 1
        return ans
