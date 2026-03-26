class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans, curr, left = 0, 0, 0
        for right in range(len(s)):
            curr += abs(ord(s[right]) - ord(t[right]))
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans

'''
Approach: Start with two pointers. Keep increasing window till cost is less than maxCost.
Shrink it if cost surpasses maxCost. Keep global variable to store maximum sized window.
'''
