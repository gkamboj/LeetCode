class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        maxf, ans, start, end = 0, 0, 0, 0
        while end < len(s):
            counter[s[end]] += 1
            maxf = max(maxf, counter[s[end]])
            while (end - start + 1) > maxf + k:
                counter[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans
