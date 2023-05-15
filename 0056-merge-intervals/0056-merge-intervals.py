class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result, currInterval = [], intervals[0]
        for interval in intervals[1:]:
            if not (currInterval[1] < interval[0] or interval[1] < currInterval[0]):
                currInterval[1] = max(interval[1], currInterval[1])
                currInterval[0] = min(interval[0], currInterval[0])
            else:
                result.append(currInterval)
                currInterval = interval
        result.append(currInterval)
        return result