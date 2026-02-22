class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda val:val[0])
        ans, curr_end = 0, intervals[0][1]
        for ind in range(1, len(intervals)):
            start, end = intervals[ind]
            if curr_end <= start:
                curr_end = end
            else:
                ans += 1
                curr_end = min(curr_end, end)
        return ans

# Approach: Sort the intervals wrt their start. For every overlap, remove the interval with higher end value (so as to avoid maximum overlapping) and increment answer.
# In case of no overlap, update curr_end variable to current end.
