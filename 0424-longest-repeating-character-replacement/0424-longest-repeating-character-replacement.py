class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = max_freq = end = ans = 0
        counter = defaultdict(int)
        while end < len(s):
            counter[s[end]] += 1
            max_freq = max(max_freq, counter[s[end]])

            while (end - start + 1) - max_freq > k and start <= end:
                counter[s[start]] -= 1
                start += 1
        
            ans = max(ans, end - start + 1)
            end += 1
    
        return ans
