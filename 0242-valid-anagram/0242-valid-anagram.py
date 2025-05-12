class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = defaultdict(int), defaultdict(int)
        for ind in range(len(s)):
            s_dict[s[ind]] += 1
            t_dict[t[ind]] += 1
        return s_dict == t_dict