class Solution {
    public int reverse(int x) {
        int ans = 0;
        boolean isNegative = false;
        if (x < 0) {
            x *= -1; //Changing negative number to positive as start to avoid handling negative cases separately
            isNegative = true;
        }
        while (x > 0) {
            if (Integer.MAX_VALUE / 10 < ans) { //If there is overflow, it will be caused by: 
                return 0;   // ans = ans * 10 i.e. multiplying ans by 10 will take it beyond max int
            }       //So, before multiplying, we can check if ans*10 > max_int => max_int/10 < ans
            int rem = x % 10;
            ans = ans * 10 + rem;
            x = x / 10;
        }
        return isNegative ? -1 * ans : ans;
    }
}

// Approach: Explained in comments alongside code See https://leetcode.com/problems/reverse-integer/discuss/4060/My-accepted-15-lines-of-code-for-Java/649167 for more detail.