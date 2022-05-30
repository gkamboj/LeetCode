class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, ans, curr = 0, len(nums) + 1, 0
        for end in range(len(nums)):
            curr += nums[end]
            while curr >= target:
                ans = min(ans, end - start + 1)
                curr -= nums[start]
                start += 1
        return ans if ans != len(nums) + 1 else 0