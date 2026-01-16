class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = defaultdict(int)
        for ind in range(len(s)):
            freq[s[ind]] += 1
            freq[t[ind]] -= 1
        for val in freq.values():
            if val:
                return False
        return True
