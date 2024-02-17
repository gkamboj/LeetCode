class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict, tDict = defaultdict(int), defaultdict(int)
        for char in s:
            sDict[char] += 1
        for char in t:
            tDict[char] += 1
        return sDict == tDict
        