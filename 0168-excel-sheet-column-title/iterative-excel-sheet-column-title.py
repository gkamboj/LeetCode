class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + ord('A')) + ans
            columnNumber //= 26
        return ans
        
#Approach: This is equivalent to decimal to binary conversion with base 26. Note that unlike base 10 where we have decimals from 0 to 9, here we have 1 (A) to 26 (Z). To make the conversion simpler, we can change this range to 0 to 25 by reducing A by 1 in every iteration.
