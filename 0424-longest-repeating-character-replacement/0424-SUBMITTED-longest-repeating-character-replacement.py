class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        ans, start, end = 0, 0, 0
        while end < len(s):
            counter[s[end]] += 1
            
            while (end - start + 1) - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
            end += 1
        
        return ans

# Approach: Use sliding window with both pointers starting at 0, and keep maintaining
# the counter map to store frequency. At every step, if difference between window
# size and the maximum frequency is more than k, keep moving "start" to right till
# the difference becomes <= k. Continue whole of this till "end" reaches the last
# index of s, with check for ans as the window size.

# Optimisation: Since we need the maximum window size, we can skip the window shrinking
# part, and focus on always moving the window or increasing it. This can reduce the
# complexity from O(26n) to O(n) as we won't need to find max(counter.values()) everytime.
# Instead, we can maintain the global maximum frequency and update only when existing max
# is surpassed.
# Refer Neetcode solution and video (https://neetcode.io/problems/longest-repeating-substring-with-replacement) for more explanation on this.
