class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans, carry, neg = 0, 0, 1
        if a == 0: return b
        if b == 0: return a
        if a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
            neg = -1
        elif a * b < 0:
            if abs(a) > b and a < 0:
                a = abs(a)
                b = -1 * b
                neg = -1
            elif abs(b) > b and b < 0:
                b = abs(a)
                a = -1 * a
                neg = -1
                
        for i in range(32):
            aCurrBit = (a >> i) & 1
            bCurrBit = (b >> i) & 1
            currXor = aCurrBit ^ bCurrBit
            ans |= ((currXor ^ carry) << i)
            carry = (aCurrBit & bCurrBit) | (currXor & carry)
        return ans * neg