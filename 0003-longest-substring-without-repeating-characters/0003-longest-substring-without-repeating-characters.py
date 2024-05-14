class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, start, counter = 0, 0, defaultdict(int)
        for ind, char in enumerate(s):
            if char in counter and counter[char] >= start:
                # Characters before start index are irrelevant, so update start only if repeated char
                # is after index start
                start = counter[char] + 1
            # else:
            ans = max(ans, ind - start + 1)
            counter[char] = ind
        return ans
    
'''
Approach: Use sliding window with start pointer and current pointer. Use dictionary to store last index 
occurence of character. Whenever a character is repeated, update the start pointer.
'''