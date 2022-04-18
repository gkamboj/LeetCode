class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        absx = abs(x)
        while absx > 0:
            rem = absx % 10
            ans = ans * 10 + rem
            absx //= 10
        if ans > 2 ** 31 - 1:
            return 0
        if x < 0:
            ans *= -1
        return ans