class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0 or b < 0: return a + b
        ans = carry = 0
        for i in range(11):
            a_bit, b_bit = (a >> i) & 1, (b >> i) & 1
            ans |= (a_bit ^ b_bit ^ carry) << i
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
        return ans