class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        List<int[]> mergedList = new ArrayList<>();
        Arrays.sort(intervals, Comparator.comparingInt(arr -> arr[0]));

        int low = intervals[0][0];
        int high = intervals[0][1];

        for(int[] interval : intervals) {
            if(interval[0] > high) {
                mergedList.add(new int[] {low, high});
                low = interval[0];
                high = interval[1];
            } else {
                high = Math.max(interval[1], high);
            }
        }
        mergedList.add(new int[]{low, high});

        return mergedList.toArray(new int[mergedList.size()][]);
    }
}