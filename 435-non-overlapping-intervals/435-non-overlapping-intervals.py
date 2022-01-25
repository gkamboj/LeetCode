class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key = lambda interval: interval[1])
        print(intervals)
        currEnd, ans = intervals[0][1], 0
        for interval in intervals[1:]:
            if interval[0] < currEnd:
                currEnd = min(interval[1], currEnd)
                ans += 1
            else:
                currEnd = interval[1]
        return ans
    
#Approach: Sort the intervals wrt their start. For every overlap, remove the interval with higher end value (so as to avoid maximum overlapping) and increment answer. In case of no overlap, update currEnd variable to current end.

#Note: For overlap, start should be less than end of other interval. There is no overlap on equality. For eg., there is no overlap for [1,2] & [2,3]