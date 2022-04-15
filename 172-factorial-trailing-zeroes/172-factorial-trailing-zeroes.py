class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            count += n // 5
            n //= 5
        return count
    
#Approach: Every 0 in factorial is contributed by factors 5 and 2. Also, in a factorial factorisation, powerof 5 < power of 2, so just count the power of 5 to get the answer.