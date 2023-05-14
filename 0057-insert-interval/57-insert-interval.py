class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals 
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        ans = []
        newIntervalAdded = False
        for interval in intervals:
            if newIntervalAdded is True or interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                ans.append(interval)
                newIntervalAdded = True
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
        if newIntervalAdded is False:
            ans.append(newInterval)
        return ans
                    
                
        