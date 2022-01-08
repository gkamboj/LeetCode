class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2: return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0: return []
        result = []
        prev = nums[0]
        for (ind, num) in enumerate(nums[:-2]):
            if(ind > 0 and num == prev): continue
            result += self.twoSum(nums[ind + 1:], num)
            prev = num
        return result
        
    def twoSum(self, nums, sum):
        start = 0
        end = len(nums) - 1
        res = []
        while start < end:
            if nums[start] + nums[end] < -1*sum:
                start += 1
            elif nums[start] + nums[end] > -1*sum:
                end -= 1
            else:
                res.append([nums[start], nums[end], sum])
                while start < end and nums[start] == nums[start + 1]: start += 1
                while start < end and nums[end] == nums[end - 1]: end -= 1
                start += 1
                end -= 1
        return res