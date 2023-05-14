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
    
#Approach: Addition of two integers can be thought of adding them bit by bit and can be sub divided into two operations - adding respective bits & considering carry over part.
#Addition of respective bits can be calculated from XOR and overall result for bit = xor ^ carry i.e. aBit ^ bBit ^ carry. 
#To find carry: carry cann be 1 or 0 - 1 if atleast two out of aBit, bBit and previous carry are 1. To simplify, note that carry = (aCurrBit & bCurrBit) | (xor & carry)

#Note: We are handling cases with negative answers explicitly because unlike Java, there is no cyclic overflow in Python. 
#Note: Since we are comparing a and b with >/< signs, it's equivalent to using +/- sign which is what we really have to avoid. So, this solution may be considered invalid. Prefer writing in Java for this.