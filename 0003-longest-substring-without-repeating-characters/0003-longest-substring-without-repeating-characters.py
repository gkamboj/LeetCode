class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, ans, curr = 0, 0, {}
        for ind, char in enumerate(s):
            if char in curr and start <= curr[char]:
                start = curr[char] + 1
            ans = max(ans, ind - start + 1)
            curr[char] = ind
        return ans