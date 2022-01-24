class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key = lambda interval: interval[1])
        print(intervals)
        high, ans = intervals[0][1], 1
        for interval in intervals[1:]:
            if interval[0] >= high:
                high = interval[1]
                ans += 1
        return len(intervals) - ans