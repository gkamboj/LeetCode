class Solution {
    
    /*public int singleNumber(int[] nums) {
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            int currBits = 0;
            for(int ind = 0; ind < nums.length; ind++) {
                if(((nums[ind] >> i) & 1) == 1) {
                    currBits += 1;
                }
            }
            if(currBits % 3 == 1) {
                ans |= 1 << i;
            }
        }
        return ans;
    }*/
    
    public int singleNumber(int[] nums) {
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            int currBits = 0;
            for(int ind = 0; ind < nums.length; ind++) {
                if((nums[ind] & (1 << i)) == (1 << i)) {
                    currBits += 1;
                }
            }
            if(currBits % 3 == 1) {
                ans |= 1 << i;
            }
        }
        return ans;
    }
}

//Approach: For every 32 bits, count number of set bits. If it's not multiple of 3, then this bit is set for our answer. Find every set bit of answer.

//Note-1: Use == in line-24 instead of '> 1'
