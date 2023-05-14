class Solution {
    public int maxChunksToSorted(int[] arr) {
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        int ans = 0, sortedSum = 0, currSum = 0;
        for (int i = 0; i < arr.length; i++) {
            sortedSum += sortedArr[i];
            currSum += arr[i];
            if (sortedSum == currSum) {
                ans += 1;
            }
        }
        return ans;
    }
}