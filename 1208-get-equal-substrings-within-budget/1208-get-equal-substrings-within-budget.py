class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans, curr, i, j = 0, 0, 0, 0
        while i <= j < len(s):
            if (diff := abs(ord(s[j]) - ord(t[j]))) > maxCost:
                i = j + 1
                curr = 0
            else:
                curr += diff
                while curr > maxCost and i < j:
                    curr -= abs(ord(s[i]) - ord(t[i]))
                    i += 1
                ans = max(ans, j - i + 1)
            j += 1
        return ans

'''
Approach: Start with two pointers. Keep increasing window till cost is less than maxCost.
Shrink it if cost surpasses maxCost. Keep global variable to store maximum sized window.
'''