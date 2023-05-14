class Solution {
    //This is divide and conquer approach
    //Check other submissions for more approaches
    
    public int maxSubArray(int[] nums) {    
        int length = nums.length;
        return getMaxSubArraySum(nums, 0, length - 1);
    }
    
    public int getMaxSubArraySum(int[] nums, int start, int end) {
        if(start == end) {
            return nums[start];
        }
        
        int mid = (start + end) / 2;
        
        int midLeftMax = Integer.MIN_VALUE;
        int midRightMax = Integer.MIN_VALUE;
        
        int sum = 0;
        for(int i = mid; i >= start; i--) {
            sum += nums[i];
            if(midLeftMax < sum) {
                midLeftMax = sum;
            }
        }
        
        sum = 0;
        for(int i = mid + 1; i <= end; i++) {
            sum += nums[i];
            if(midRightMax < sum) { 
                midRightMax = sum;
            }
        }
        return Math.max(Math.max(getMaxSubArraySum(nums, start, mid), getMaxSubArraySum(nums, mid + 1, end)), midRightMax + midLeftMax);
        
    }
}
