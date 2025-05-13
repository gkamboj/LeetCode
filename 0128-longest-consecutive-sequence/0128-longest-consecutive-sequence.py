class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = 1
        ans = 0
        for num in mp:
            if num - 1 not in mp:
                count = 1
                while num + 1 in mp:
                    count += 1
                    num += 1
                ans = max(ans, count)
        return ans