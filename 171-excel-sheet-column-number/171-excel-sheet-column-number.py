class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, power = 0, 0
        for char in columnTitle[::-1]:
            ans += (26 ** power) * (ord(char) - ord('A') + 1)
            power += 1
        return ans