class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict, tDict = defaultdict(int), defaultdict(int)
        for ind in range(len(s)):
            sDict[s[ind]] += 1
            tDict[t[ind]] += 1
        return sDict == tDict
        