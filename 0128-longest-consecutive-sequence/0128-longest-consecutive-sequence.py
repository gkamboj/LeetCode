class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset, ans = set(nums), 0
        for num in nset:
            if (num - 1) not in nset:
                curr = 1
                while (num + 1) in nset:
                    num += 1
                    curr += 1
                ans = max(ans, curr)
        return ans