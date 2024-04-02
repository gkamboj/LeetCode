class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        for ind in range(len(s)):
            if t[ind] in char_dict:
                if char_dict[t[ind]] != s[ind]:
                    return False
            else:
                if s[ind] in char_dict.values():
                    return False
                char_dict[t[ind]] = s[ind]
        return True