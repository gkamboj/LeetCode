class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, ans = 0, 0
        mp = {}
        for ind in range(len(s)):
            char = s[ind]
            if mp.get(char, -1) >= start:
                start = mp.get(char, -1) + 1
            mp[char] = ind
            ans = max(ans, ind + 1 - start)
        return ans
