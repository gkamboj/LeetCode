class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans, sign = 0, 1
        if divisor < 0:
            sign = -sign
            divisor = abs(divisor)
        if dividend < 0:
            sign = -sign
            dividend = abs(dividend)
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)
                ans += (1 << i)
        ans *= sign
        ans = min(ans, 2 ** 31 - 1)
        ans = max(ans, -2 ** 31)
        return ans
            
#Approach: Firstly check both numbers for negative sign and consider their absolute value for doing division. Now, to do the division, we can check for every bit starting from most significant bit, and whenever divisor * 2^i <= dividend for any ith bit, consider ith bit as part of answer and reduce divisor by diviro * 2^i (Since multiplication can't be used, use << operator for this). To further understand why this works, consider following example:
# 94 / 6 (considering from i = 5 to i = 0 only for this example):
# 6 * 2^5 <= 94 => No
# 6 * 2^4 <= 94 => No
# 6 * 2^3 <= 94 => Yes => ans = 0 + 2^3, divisor = 94 - 6 * 2^3 = 46
# 6 * 2^2 <= 46 => Yes => ans = 8 + 2^2, divisor = 46 - 6 * 2^2 = 22
# 6 * 2^1 <= 22 => Yes => ans = 12 + 2^1, divisor = 22 - 6 * 2^1 = 10
# 6 * 2^0 <= 10 => Yes => ans = 14 + 2^0 = 15, divisor = 10 - 6 * 2^0 = 4