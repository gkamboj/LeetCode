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