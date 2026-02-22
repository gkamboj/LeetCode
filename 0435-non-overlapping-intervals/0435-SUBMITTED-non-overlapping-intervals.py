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

# Approach: Sort the intervals wrt their start. For every overlap, remove the interval with the higher end value (so as to avoid maximum overlapping) and increment the ans.
# In case of no overlap, update the curr_end variable to the current end.
