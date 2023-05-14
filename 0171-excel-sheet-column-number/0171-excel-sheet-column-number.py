class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, titleLen = 0, len(columnTitle)
        for i in range(len(columnTitle)):
            ans = ans + (26 ** i) * (ord(columnTitle[-1-i]) - ord('A') + 1)
        return ans