class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        ans, start, end = 0, 0, 0
        while end < len(s):
            counter[s[end]] += 1
            max_freq = max(counter.values())
            while (end - start + 1) - max_freq > k:
                counter[s[start]] -= 1
                start += 1
                max_freq = max(counter.values())
            ans = max(ans, end - start + 1)
            end += 1
        return ans
