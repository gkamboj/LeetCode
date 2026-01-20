class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        start, end, maxfreq, ans = 0, 0, 0, 0
        while end < len(s):
            char = s[end]
            counter[char] += 1
            maxfreq = max(maxfreq, counter[char])
            while (end - start + 1) - maxfreq > k:
                counter[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans
