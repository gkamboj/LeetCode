class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set, ans = set(nums), 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                while curr + 1 in nums_set:
                    curr += 1
                ans = max(ans, curr - num + 1)
        return ans