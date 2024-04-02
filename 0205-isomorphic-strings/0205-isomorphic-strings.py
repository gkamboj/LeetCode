class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        char_dict = {}
        for ind in range(len(s)):
            if t[ind] not in char_dict:
                char_dict[t[ind]] = s[ind]
            elif char_dict[t[ind]] != s[ind]:
                return False
        return True
    
""" Approach: If number of unique characters of bothe strings are not matching, return False as strings cannot
be isomorphic in that case. Create a map to store mapping of t's chars with chars of s. If at anytime, s[ind] 
does not match with existing value of dict[t[ind]], return False """