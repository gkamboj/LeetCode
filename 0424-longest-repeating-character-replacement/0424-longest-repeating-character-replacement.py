class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        ans, start, end = 0, 0, 0
        while end < len(s):
            counter[s[end]] += 1
            max_char = max(counter, key=counter.get)
            if (end - start + 1) - counter[max_char] <= k:
                ans = max(ans, end - start + 1)
                end += 1
            else:
                counter[s[start]] -= 1
                counter[s[end]] -= 1
                start += 1
        return ans
