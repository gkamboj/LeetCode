class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = -1 if x < 0 else 1
        x = abs(x)
        while x:
            rem = x % 10
            x //= 10
            ans  = (ans * 10) + rem
            if ans >= 2 ** 31:
                return 0
        return ans * neg
