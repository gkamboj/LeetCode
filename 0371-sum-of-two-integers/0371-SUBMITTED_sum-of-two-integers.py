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

# Approach: Addition of two integers can be thought of adding them bit by bit and can be sub divided into two operations -
# adding respective bits & considering carry over part.
# Addition of respective bits can be calculated from XOR = a_bit ^ b_bit ^ carry. 
# To find carry: carry cann be 1 or 0: 1 if atleast two out of a_bit, b_bit and previous carry are 1.

# Note: We are handling cases with negative answers explicitly because unlike Java, there is no cyclic overflow in Python. 

# Note: Since we are comparing a and b with >/< signs, it's equivalent to using +/- sign which is what we really have to avoid.
# So, this solution may be considered invalid. Prefer writing in Java for this.
