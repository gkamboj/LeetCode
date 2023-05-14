class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength, ans, minStr = 100000, '', ''
        for s in strs:
            if minLength > len(s):
                minStr = s
                minLength = len(s)
        for i in range(minLength):
            for s in strs:
                if s[i] != minStr[i]:
                    return ans
            ans += minStr[i]
        return ans
