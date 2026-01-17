class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, curr, start = 0, {}, 0
        for ind, char in enumerate(s):
            if curr.get(char, -1) >= start:
                # Characters before the start index are irrelevant, so update start only if repeated char
                # is after index start
                start = curr[char] + 1
            ans = max(ans, ind - start + 1)
            curr[char] = ind
        return ans
    
'''
Approach: Use a sliding window with a start pointer and a current pointer. Use a dictionary to store the last index 
occurrence of a character. Whenever a character is repeated, update the start pointer.
'''
