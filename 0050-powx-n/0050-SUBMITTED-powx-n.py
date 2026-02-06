class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return 0
        if not n:
            return 1
        
        ans, power = 1, abs(n)
        
        while power:
            if power & 1:
                ans *= x
            x *= x
            power >>= 1
        
        return ans if n > 0 else 1/ans

# Approach: Keep squaring x and halving n. Multiple ans with x whenever n becomes odd. Handle negative cases before returning.
# Refer NC iterative solution for more details.
