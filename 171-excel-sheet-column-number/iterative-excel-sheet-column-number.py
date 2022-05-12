class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans += (ord(columnTitle[-i-1]) - ord('A') + 1) * (26 ** i)
        return ans
    
# Approach: Treat the input as number in base-26 number system, and convert it to decimal number. Use ASCII value to find the value of character in base-26 system.
