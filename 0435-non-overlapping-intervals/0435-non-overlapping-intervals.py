class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda val:val[0])
        temp = [intervals[0]]
        for ind in range(1, len(intervals)):
            start, end = intervals[ind]
            if temp[-1][1] <= start:
                temp.append(intervals[ind])
            else:
                temp[-1][1] = min(temp[-1][1], end)
        return len(intervals) - len(temp)