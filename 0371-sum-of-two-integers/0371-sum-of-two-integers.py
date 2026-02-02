class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = carry = 0
        neg = 1
        if a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
            neg = -1
        elif a < 0 or b < 0:
            if a < 0 and abs(a) > b:
                neg = -1
                b = -1 * b
                a = abs(a)
            elif b < 0 and abs(b) > a:
                neg = -1
                b = abs(b)
                a = -1 * a

        for i in range(11):
            a_bit, b_bit = (a >> i) & 1, (b >> i) & 1
            ans |= (a_bit ^ b_bit ^ carry) << i
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
        return ans * neg