class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda val:val[0])
        ans = [intervals[0]]
        for ind in range(1, len(intervals)):
            val = intervals[ind]
            if ans[-1][1] < val[0]:
                ans.append(val)
            else:
                ans[-1][1] = max(ans[-1][1], val[1])
        return ans