class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        char_occ = {} #to store last occurence of visited characters
        for i in range(0,len(s)):
            if s[i] in char_occ and char_occ[s[i]] >= start:
                start = char_occ[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            char_occ[s[i]] = i
            
        return max_len