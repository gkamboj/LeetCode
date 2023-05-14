class Solution {
    public int reverse(int x) {
        int ans = 0;
        boolean isNegative = false;
        if (x < 0) {
            x *= -1;
            isNegative = true;
        }
        while (x > 0) {
            if (Integer.MAX_VALUE / 10 < ans) {
                return 0;
            }
            int rem = x % 10;
            ans = ans * 10 + rem;
            x = x / 10;
        }
        return isNegative ? -1 * ans : ans;
    }
}