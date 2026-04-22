class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp, start, ans = {}, 0, 0
        
        for ind, char in enumerate(s):
            while char in mp and mp[char] >= start:
                start += 1
            mp[char] = ind
            ans = max(ans, ind - start + 1)

        return ans