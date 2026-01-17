class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, curr, start = 0, {}, 0
        for ind, char in enumerate(s):
            if curr.get(char, -1) >= start:
                start = curr[char] + 1
            ans = max(ans, ind - start + 1)
            curr[char] = ind
        return ans