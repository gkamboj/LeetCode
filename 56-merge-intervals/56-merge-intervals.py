class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        ans = []
        intervals = sorted(intervals, key = lambda interval: interval[0])
        low, high = intervals[0][0], intervals[0][1]
        for interval in intervals:
            if interval[0] <= high:
                high = max(interval[1], high)
            else:
                ans.append([low, high])
                high = interval[1]
                low = interval[0]
        ans.append([low, high])
        return ans
    
#Approach: Sort the intervals by start. Traverse the array and keep updating high till there is overlap. Initialise low and high after adding to ans once there is no overlap.