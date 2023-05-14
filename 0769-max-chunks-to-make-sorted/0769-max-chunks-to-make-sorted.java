class Solution {
    public int maxChunksToSorted(int[] arr) {
        int ans = 0;
        int curr = 0;
        for (int i = 0; i < arr.length; i++) {
            curr += arr[i];
            if (i * (i + 1) == 2 * curr) {
                ans += 1;
            }
        }
        return ans;
        
    }
}