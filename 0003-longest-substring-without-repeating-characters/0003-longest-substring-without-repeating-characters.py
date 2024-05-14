class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, start, counter = 0, 0, defaultdict(int)
        for ind, char in enumerate(s):
            if char in counter and counter[char] >= start:
                start = counter[char] + 1
            else:
                ans = max(ans, ind - start + 1)
            counter[char] = ind
        return ans