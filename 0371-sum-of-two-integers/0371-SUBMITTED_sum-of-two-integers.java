class Solution {
    public int getSum(int a, int b) {
        int carry, ans, aCurrBit, bCurrBit, xor;
        carry = ans = 0;
        for(int i = 0; i < 32; i++) {
            aCurrBit = (a >> i) & 1;
            bCurrBit = (b >> i) & 1;
            xor = aCurrBit ^ bCurrBit;
            ans |= ((xor ^ carry) << i);
            carry = (aCurrBit & bCurrBit) | (xor & carry);
        }
        return ans;
    }
}

// Approach: Addition of two integers can be thought of adding them bit by bit and can be sub divided into two operations -
// adding respective bits & considering carry over part.
// Addition of respective bits can be calculated from XOR = aBit ^ bBit ^ carry. 
// To find carry: carry cann be 1 or 0 - 1 if atleast two out of aBit, bBit and previous carry are 1. To simplify, note that carry = (aCurrBit & bCurrBit) | (xor & carry)

// Note: Same approach won't work directly in Python as there is no cyclic overflow like Java in Python. So, negative number cases needs to be handled sparately there. 
