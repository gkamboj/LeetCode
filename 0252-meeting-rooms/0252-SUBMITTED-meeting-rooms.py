"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for ind, val in enumerate(intervals[1:], start=1):
            if val.start < intervals[ind - 1].end:
                return False
        return True
