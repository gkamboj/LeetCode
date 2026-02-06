class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x or x == 1:
            return x
        if x == -1:
            return -1 if n % 2 else 1
        if not n:
            return 1
        power, ans = abs(n), x
        while power > 1:
            ans *= x
            power -= 1
            curr = ans if n > 0 else 1/ans
            if -0.00001 < curr < 0.00001:
                return 0
        return ans if n > 0 else 1/ans
