class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        ans, start, end, max_f = 0, 0, 0, 0
        while end < len(s):
            counter[s[end]] += 1
            max_f = max(counter[s[end]], max_f)
            
            while (end - start + 1) - max_f > k:
                counter[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
            end += 1
        
        return ans

# This is optimised approach of the other SUBMITTED submission. Since we need the maximum
# window size, we can skip the window shrinking part, and focus on always moving the
# window or increasing it. This can reduce the complexity from O(26n) to O(n) as we won't
# need to find max(counter.values()) everytime. Instead, we can maintain the global
# maximum frequency and update only when existing max is surpassed.
# Refer Neetcode solution and video (https://neetcode.io/problems/longest-repeating-substring-with-replacement) for more explanation on this.
